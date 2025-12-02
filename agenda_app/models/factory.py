from models.activity import WorkActivity, StudyActivity, PersonalActivity

class ActivityFactory:
    @staticmethod
    def create_activity(activity_type, title, description, deadline, priority):
        if activity_type == "work":
            return WorkActivity(title, description, deadline, priority)
        elif activity_type == "study":
            return StudyActivity(title, description, deadline, priority)
        elif activity_type == "personal":
            return PersonalActivity(title, description, deadline, priority)
        else:
            raise ValueError("Tipo de atividade inválido")