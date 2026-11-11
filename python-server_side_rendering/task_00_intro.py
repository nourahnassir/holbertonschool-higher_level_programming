#!/usr/bin/python3


def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values, fallback to "N/A"
        name = attendee.get("name")
        name = name if name is not None else "N/A"

        event_title = attendee.get("event_title")
        event_title = event_title if event_title is not None else "N/A"

        event_date = attendee.get("event_date")
        event_date = event_date if event_date is not None else "N/A"

        event_location = attendee.get("event_location")
        event_location = event_location if event_location is not None else "N/A"

        # Construct content using string replacement
        content = template.replace("{name}", name)
        content = content.replace("{event_title}", event_title)
        content = content.replace("{event_date}", event_date)
        content = content.replace("{event_location}", event_location)

        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
