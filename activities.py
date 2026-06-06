from datetime import datetime


class Activity:

    def __init__(
        self,
        activity_id=None,
        user_id=None,
        activity_name="",
        duration=0
    ):

        self.activity_id = activity_id
        self.user_id = user_id
        self.activity_name = activity_name
        self.duration = duration
        self.activity_date = datetime.now()

    def update_duration(self, duration):

        self.duration = duration

    def get_duration_hours(self):

        return round(
            self.duration / 60,
            2
        )

    def to_dict(self):

        return {
            "activity_id": self.activity_id,
            "user_id": self.user_id,
            "activity_name": self.activity_name,
            "duration": self.duration,
            "activity_date": str(self.activity_date)
        }

    def display_activity(self):

        print(
            self.activity_name,
            self.duration,
            self.activity_date
        )

    def __str__(self):

        return f"Activity({self.activity_name})"