#!/usr/bin/env python3
import os

def main():
    # Ask the user for the name
    name = input("Enter the name (e.g. 'What is a Database?'): ").strip()

    # Ask for the type (webpage or video)
    note_type = input("Is this for a Webpage or a Video? ").strip().lower()

    # Validate input
    if note_type not in ["webpage", "video"]:
        print("Invalid type. Please enter either 'Webpage' or 'Video'.")
        return

    # Format the filename
    type_label = "Webpage Notes" if note_type == "webpage" else "Video Notes"
    filename = f"{name.replace(' ', '_')}_{type_label.replace(' ', '_')}.py"

    # Ensure the notes directory exists
    notes_dir = "course_notes"
    os.makedirs(notes_dir, exist_ok=True)

    # Full path for the file
    file_path = os.path.join(notes_dir, filename)

    # Create the file contents
    contents = f'''""" {name} {type_label}

"""'''

    # Write to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(contents)

    # Confirm creation
    print(f"Created file: {file_path}")

if __name__ == "__main__":
    main()