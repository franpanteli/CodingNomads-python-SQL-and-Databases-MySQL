# course_automation_program.py

#imports
import sys
import os

while True:
    #print menu 
    print("\n=== Course Automation Menu ===")
    print("1. Push all changes to GitHub")
    print("2. Create notes")
    print("3. Edit file with a given directory")
    print("4. Open GitHub repository in Chrome")
    print("5. Open project in PyCharm")
    print("6. Delete file with given directory")
    print("7. Clear terminal")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        from course_automation_scripts import auto_git_push
        print("\nRunning auto_git_push...")
        auto_git_push.git_push()  # Make sure auto_git_push.py has a function named git_push()
    elif choice == "2":
        from course_automation_scripts import create_notes
        print("\nRunning create_notes...")
        create_notes.main()  # Make sure create_notes.py has a function named main()
    elif choice == "3":
        from course_automation_scripts import open_file_in_pycharm
        print("\nRunning open_file_in_pycharm...")
        open_file_in_pycharm.main() 
    elif choice == "4":
        from course_automation_scripts import open_github_repo
        print("\nOpening GitHub repository...")
        open_github_repo.open_repo()  # Make sure open_github_repo.py has a function named open_repo()
    elif choice == "5":
        from course_automation_scripts import open_project_in_pycharm
        print("\nOpening project in PyCharm...")
        open_project_in_pycharm.open_project()  # Make sure open_project_in_pycharm.py has a function named open_project()
    elif choice == "6":
        from course_automation_scripts import delete_file
        print("\nDeleting file...")
        delete_file.main()
    elif choice == "7":
        from course_automation_scripts import clear_terminal
        clear_terminal.main()
    elif choice == "8":
        print("Exiting program. Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
