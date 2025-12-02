from datetime import datetime

class Activity:
    def __init__(self, title, description, deadline, priority):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return f"{self.title} — prioridade {self.priority}"

class WorkActivity(Activity):
    pass

class StudyActivity(Activity):
    pass

class PersonalActivity(Activity):
    pass