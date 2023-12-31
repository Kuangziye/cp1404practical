class Project:
    def __init__(self, name, datetime, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime("%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def display_project(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority},estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}% "

