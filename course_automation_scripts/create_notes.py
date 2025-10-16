#!/usr/bin/env python3

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

    # Create the file contents
    contents = f'''""" {name} {type_label}

"""'''

    # Write to the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents)

    # Confirm creation
    print(f"Created file: {filename}")

if __name__ == "__main__":
    main()
