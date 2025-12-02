class Agenda:
    def __init__(self, strategy):
        self.activities = []
        self.strategy = strategy
        self.observers = []

    # -----------------------
    # MÉTODOS DE OBSERVER
    # -----------------------

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, activity):
        for observer in self.observers:
            observer.update(activity)

    # -----------------------
    # MÉTODOS PRINCIPAIS
    # -----------------------

    def add_activity(self, activity):
        self.activities.append(activity)
        self.notify(activity)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_sorted_activities(self):
        """Aplica a estratégia atual (Strategy Pattern)"""
        return self.strategy.sort(self.activities)