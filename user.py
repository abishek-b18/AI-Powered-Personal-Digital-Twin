from datetime import datetime


class User:

    def __init__(
        self,
        user_id=None,
        fullname="",
        email="",
        password="",
        created_at=None
    ):

        self.user_id = user_id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.created_at = created_at or datetime.now()

    def to_dict(self):

        return {
            "user_id": self.user_id,
            "fullname": self.fullname,
            "email": self.email,
            "created_at": str(self.created_at)
        }

    def get_profile_summary(self):

        return {
            "name": self.fullname,
            "email": self.email,
            "member_since": str(self.created_at)
        }

    def update_profile(
        self,
        fullname=None,
        email=None
    ):

        if fullname:
            self.fullname = fullname

        if email:
            self.email = email

    def change_password(
        self,
        new_password
    ):

        self.password = new_password

    def display_user(self):

        print("User ID:", self.user_id)
        print("Name:", self.fullname)
        print("Email:", self.email)
        print("Created:", self.created_at)

    def __str__(self):

        return f"User({self.user_id}, {self.fullname})"