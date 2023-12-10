from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

ProgrammingLanguage = [python, ruby, visual_basic]
for programming in ProgrammingLanguage:
    print(programming)

print("The dynamically typed languages are:")
for programming in ProgrammingLanguage:
    if programming.is_dynamic():
        print(programming.programming_name)