import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendee list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Get values or "N/A" if missing or None
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        personalized_invite = template
        personalized_invite = personalized_invite.replace("{name}", name)
        personalized_invite = personalized_invite.replace("{event_title}", event_title)
        personalized_invite = personalized_invite.replace("{event_date}", event_date)
        personalized_invite = personalized_invite.replace("{event_location}", event_location)

        # Generate output filename
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(personalized_invite)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")