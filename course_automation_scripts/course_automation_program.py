# course_automation_program.py

import sys
import os
from course_automation_scripts import auto_git_push, create_notes, open_github_repo, open_project_in_pycharm


def main():
    while True:
        print("\n=== Course Automation Menu ===")
        print("1. Push all changes to GitHub")
        print("2. Create notes")
        print("3. Open GitHub repository in Chrome")
        print("4. Open project in PyCharm")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nRunning auto_git_push...")
            auto_git_push.git_push()  # Make sure auto_git_push.py has a function named git_push()
        elif choice == "2":
            print("\nRunning create_notes...")
            create_notes.main()  # Make sure create_notes.py has a function named main()
        elif choice == "3":
            print("\nOpening GitHub repository...")
            open_github_repo.open_repo()  # Make sure open_github_repo.py has a function named open_repo()
        elif choice == "4":
            print("\nOpening project in PyCharm...")
            open_project_in_pycharm.open_project()  # Make sure open_project_in_pycharm.py has a function named open_project()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()