class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.programming_name = name
        self.programming_type = typing
        self.reflection = reflection
        self.programming_year = year

    def is_dynamic(self):
        return self.programming_type == "Dynamic"

    def __str__(self):
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.programming_name}, {self.programming_type} Typing, {reflection_str}, First appeared in {self.programming_year}"
