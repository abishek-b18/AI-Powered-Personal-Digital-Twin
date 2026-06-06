// ======================================
// AI DIGITAL TWIN MAIN JAVASCRIPT FILE
// ======================================

console.log("AI Personal Digital Twin Loaded Successfully");

// ======================================
// WELCOME MESSAGE
// ======================================

window.addEventListener("load", () => {
    showWelcomeMessage();
    generateDailyInsight();
});

// ======================================
// WELCOME ALERT
// ======================================

function showWelcomeMessage() {

    const today = new Date();

    const hour = today.getHours();

    let greeting = "Welcome";

    if(hour < 12){
        greeting = "Good Morning";
    }
    else if(hour < 18){
        greeting = "Good Afternoon";
    }
    else{
        greeting = "Good Evening";
    }

    console.log(`${greeting}! AI Digital Twin Activated.`);
}

// ======================================
// DAILY AI INSIGHTS
// ======================================

function generateDailyInsight(){

    const insights = [

        "Focus on your highest priority task first.",

        "You are most productive between 9 AM and 12 PM.",

        "Completing small tasks improves motivation.",

        "Your learning consistency is improving.",

        "Try reducing distractions for better productivity.",

        "Exercise can improve your concentration levels.",

        "Your digital twin predicts higher performance tomorrow."

    ];

    const randomInsight =
        insights[Math.floor(Math.random() * insights.length)];

    console.log("AI Insight:", randomInsight);
}

// ======================================
// PRODUCTIVITY SCORE CALCULATOR
// ======================================

function calculateProductivityScore(
    completedTasks,
    totalTasks
){

    if(totalTasks === 0){
        return 0;
    }

    return Math.round(
        (completedTasks / totalTasks) * 100
    );
}

// Example

let score =
calculateProductivityScore(8,10);

console.log("Productivity Score:", score + "%");

// ======================================
// GOAL PROGRESS FUNCTION
// ======================================

function updateGoalProgress(
    current,
    total
){

    let progress =
    Math.round((current / total) * 100);

    return progress;
}

console.log(
    "Goal Progress:",
    updateGoalProgress(7,10) + "%"
);

// ======================================
// SMART AI RECOMMENDATION
// ======================================

function generateRecommendation(score){

    if(score >= 90){
        return "Excellent work! Keep maintaining your momentum.";
    }

    if(score >= 70){
        return "Good progress. Focus on consistency.";
    }

    if(score >= 50){
        return "You are improving. Consider reducing distractions.";
    }

    return "Let's improve productivity with better planning.";
}

console.log(
    generateRecommendation(score)
);

// ======================================
// GOAL TRACKER
// ======================================

let goals = [

    {
        title: "Learn Machine Learning",
        progress: 70
    },

    {
        title: "Build Startup MVP",
        progress: 45
    },

    {
        title: "Daily Exercise",
        progress: 80
    }

];

function displayGoals(){

    goals.forEach(goal => {

        console.log(
            `${goal.title} - ${goal.progress}%`
        );

    });

}

displayGoals();

// ======================================
// ACTIVITY TRACKER
// ======================================

let activities = [

    {
        activity: "Coding",
        duration: 120
    },

    {
        activity: "Reading",
        duration: 60
    },

    {
        activity: "Exercise",
        duration: 45
    }

];

function totalActivityTime(){

    let total = 0;

    activities.forEach(item => {

        total += item.duration;

    });

    return total;
}

console.log(
    "Total Activity Time:",
    totalActivityTime(),
    "minutes"
);

// ======================================
// AI FUTURE PREDICTION
// ======================================

function predictProductivity(){

    const prediction =
        Math.floor(Math.random() * 20) + 80;

    return prediction;
}

console.log(
    "Predicted Productivity:",
    predictProductivity() + "%"
);

// ======================================
// SMART NOTIFICATION SYSTEM
// ======================================

function notifyUser(message){

    console.log(
        "Notification:",
        message
    );

}

notifyUser(
    "Remember to complete your AI project today."
);

// ======================================
// HEALTH ANALYTICS
// ======================================

function healthScore(
    sleepHours,
    exerciseMinutes
){

    let score = 0;

    if(sleepHours >= 7){
        score += 50;
    }

    if(exerciseMinutes >= 30){
        score += 50;
    }

    return score;
}

console.log(
    "Health Score:",
    healthScore(8,45)
);

// ======================================
// DIGITAL TWIN STATUS
// ======================================

function digitalTwinStatus(){

    return {

        learning: true,
        active: true,
        predictionEngine: true,
        recommendationSystem: true

    };
}

console.log(
    "Digital Twin Status:",
    digitalTwinStatus()
);

// ======================================
// DASHBOARD CLOCK
// ======================================

function updateClock(){

    const now = new Date();

    const time =
        now.toLocaleTimeString();

    const clockElement =
        document.getElementById("clock");

    if(clockElement){
        clockElement.innerHTML = time;
    }
}

setInterval(updateClock,1000);

// ======================================
// MOTIVATIONAL QUOTES
// ======================================

const quotes = [

    "Success is the sum of small efforts repeated daily.",

    "Consistency beats motivation.",

    "Your future is created by what you do today.",

    "Progress, not perfection.",

    "Discipline is the bridge between goals and achievement."

];

function randomQuote(){

    return quotes[
        Math.floor(Math.random() * quotes.length)
    ];

}

console.log(
    randomQuote()
);

// ======================================
// AI CHAT PLACEHOLDER
// ======================================

function sendMessage(message){

    return "AI Assistant: I received -> " + message;

}

console.log(
    sendMessage("How productive am I?")
);

// ======================================
// END OF FILE
// ======================================