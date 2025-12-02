from datetime import datetime

class SortByDateStrategy:
    def sort(self, activities):
        return sorted(activities, key=lambda x: x.deadline)


class SortByPriorityStrategy:
    def sort(self, activities):
        return sorted(activities, key=lambda x: x.priority, reverse=True)