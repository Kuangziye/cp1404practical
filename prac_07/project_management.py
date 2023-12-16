import datetime
from project import Project


def main():
    projects = []
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            loading_project(projects)
            choice = input(">>> ").lower()
        elif choice == "s":
            save_project(projects)
            choice = input(">>> ").lower()
        elif choice == "d":
            display_project(projects)
            choice = input(">>> ").lower()
        elif choice == "f":
            filter_project_by_date()
            choice = input(">>> ").lower()
        elif choice == "a":
            add_new_project(projects)
            choice = input(">>> ").lower()
        elif choice == "u":
            update_project(projects)
            choice = input(">>> ").lower()


def loading_project(projects):
    in_file = open('projects.txt', 'r')
    for line in in_file:
        project_line = line
        projects.append(project_line)
    in_file.close()


def save_project(projects):
    out_file = open('projects.txt', 'w')
    for project in projects:
        out_file.writelines(project)
    out_file.close()


def display_project(projects):
    print(projects)


def filter_project_by_date():
    date = input("Show projects that start after date (dd/mm/yy): ")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name:")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    display_project(projects)
    project_choice = input("Project choice: ")
    print(projects[project_choice])
    new_percentage = input("New Percentage: ")


main()
