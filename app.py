from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "digital_twin_secret_key"

DATABASE = "database.db"


# ==========================
# DATABASE CONNECTION
# ==========================

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================
# DATABASE INITIALIZATION
# ==========================

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        description TEXT,
        status TEXT DEFAULT 'Pending',
        progress INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        activity_name TEXT,
        duration INTEGER,
        activity_date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# SAMPLE DATA INSERTION
# ==========================

def insert_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    if not cursor.fetchone():

        cursor.execute("""
        INSERT INTO users(fullname,email,password)
        VALUES
        ('Abishek','abishek@gmail.com','123456'),
        ('John Doe','john@gmail.com','123456'),
        ('Alice','alice@gmail.com','123456')
        """)

        cursor.execute("""
        INSERT INTO goals(user_id,title,description,status,progress)
        VALUES
        (1,'Learn AI','Complete ML Course','In Progress',70),
        (1,'Fitness Goal','Exercise Daily','In Progress',55),
        (1,'Build Startup','Develop MVP','Pending',30)
        """)

        cursor.execute("""
        INSERT INTO activities(user_id,activity_name,duration,activity_date)
        VALUES
        (1,'Study Machine Learning',120,'2026-06-01'),
        (1,'Coding Project',180,'2026-06-02'),
        (1,'Reading Research Papers',90,'2026-06-03'),
        (1,'Exercise',45,'2026-06-04')
        """)

    conn.commit()
    conn.close()


# ==========================
# HOME PAGE
# ==========================

@app.route('/')
def home():
    return render_template('index.html')


# ==========================
# LOGIN
# ==========================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()

        conn.close()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['fullname']
            return redirect(url_for('dashboard'))

        flash("Invalid Credentials")
        return redirect(url_for('login'))

    return render_template('login.html')


# ==========================
# SIGNUP
# ==========================

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()

        try:
            conn.execute(
                """
                INSERT INTO users(fullname,email,password)
                VALUES(?,?,?)
                """,
                (fullname, email, password)
            )

            conn.commit()

            flash("Account Created Successfully")
            return redirect(url_for('login'))

        except:
            flash("Email Already Exists")

        finally:
            conn.close()

    return render_template('signup.html')


# ==========================
# DASHBOARD
# ==========================

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()

    goals = conn.execute(
        "SELECT * FROM goals WHERE user_id=?",
        (session['user_id'],)
    ).fetchall()

    activities = conn.execute(
        "SELECT * FROM activities WHERE user_id=?",
        (session['user_id'],)
    ).fetchall()

    total_goals = len(goals)
    completed = sum(goal['progress'] for goal in goals)

    productivity_score = (
        completed // total_goals
        if total_goals > 0
        else 0
    )

    conn.close()

    return render_template(
        'dashboard.html',
        goals=goals,
        activities=activities,
        productivity_score=productivity_score
    )


# ==========================
# ANALYTICS PAGE
# ==========================

@app.route('/analytics')
def analytics():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()

    activities = conn.execute(
        """
        SELECT activity_name,duration
        FROM activities
        WHERE user_id=?
        """,
        (session['user_id'],)
    ).fetchall()

    conn.close()

    labels = [row['activity_name'] for row in activities]
    values = [row['duration'] for row in activities]

    return render_template(
        'analytics.html',
        labels=labels,
        values=values
    )


# ==========================
# ADD GOAL
# ==========================

@app.route('/add_goal', methods=['POST'])
def add_goal():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    title = request.form['title']
    description = request.form['description']

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO goals
        (user_id,title,description)
        VALUES(?,?,?)
        """,
        (session['user_id'], title, description)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))


# ==========================
# ADD ACTIVITY
# ==========================

@app.route('/add_activity', methods=['POST'])
def add_activity():

    if 'user_id' not in session:
        return redirect(url_for('login'))

    activity_name = request.form['activity_name']
    duration = request.form['duration']

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO activities
        (user_id,activity_name,duration,activity_date)
        VALUES(?,?,?,?)
        """,
        (
            session['user_id'],
            activity_name,
            duration,
            datetime.now().strftime("%Y-%m-%d")
        )
    )

    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))


# ==========================
# AI INSIGHTS API
# ==========================

@app.route('/api/insights')
def insights():

    sample_insights = [
        "Your productivity increased by 15% this week.",
        "Consider allocating more time for learning.",
        "You are likely to complete your AI goal within 10 days.",
        "Exercise frequency is improving consistently.",
        "Your digital twin predicts high productivity tomorrow."
    ]

    return jsonify(sample_insights)


# ==========================
# LOGOUT
# ==========================

@app.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('home'))


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    initialize_database()
    insert_sample_data()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )