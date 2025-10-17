#!/usr/bin/env python3
import os
import re

def main():
    # Ask the user for the name
    name = input("Enter the name (e.g. 'What is a Database?'): ").strip()

    # Ask for the type (webpage or video)
    note_type = input("Is this for a Webpage or a Video? ").strip().lower()

    # Validate input
    if note_type not in ["webpage", "video"]:
        print("Invalid type. Please enter either 'Webpage' or 'Video'.")
        return

    # Format the type label
    type_label = "Webpage Notes" if note_type == "webpage" else "Video Notes"

    # Ensure the notes directory exists
    notes_dir = "course_notes"
    os.makedirs(notes_dir, exist_ok=True)

    # Determine the next number
    existing_files = os.listdir(notes_dir)
    pattern = re.compile(r"_(\d{2})\.py$")
    numbers = [int(pattern.search(f).group(1)) for f in existing_files if pattern.search(f)]
    next_number = max(numbers) + 1 if numbers else 1
    number_str = f"{next_number:02d}"

    # Create the filename
    safe_name = name.replace(' ', '_').replace('?', '')
    filename = f"{safe_name}_{type_label.replace(' ', '_')}_{number_str}.py"
    file_path = os.path.join(notes_dir, filename)

    # File contents
    contents = f'''""" {name} {type_label}

"""'''

    # Write to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(contents)

    print(f"Created file: {file_path}")

if __name__ == "__main__":
    main()