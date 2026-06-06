from datetime import datetime


class Goal:

    def __init__(
        self,
        goal_id=None,
        user_id=None,
        title="",
        description="",
        status="Pending",
        progress=0
    ):

        self.goal_id = goal_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status
        self.progress = progress
        self.created_at = datetime.now()

    def update_progress(self, value):

        self.progress = value

        if self.progress >= 100:
            self.progress = 100
            self.status = "Completed"

        elif self.progress > 0:
            self.status = "In Progress"

    def mark_completed(self):

        self.progress = 100
        self.status = "Completed"

    def get_completion_percentage(self):

        return self.progress

    def to_dict(self):

        return {
            "goal_id": self.goal_id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "progress": self.progress
        }

    def __str__(self):

        return f"Goal({self.title}, {self.progress}%)"