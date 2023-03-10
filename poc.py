import sys
import base64
import email

def convert_eml_to_email_message(file_path):
    try:
        # Open the .eml file
        with open(file_path, "r") as f:
            # Read the contents of the file
            eml_content = f.read()

        # Parse the .eml content into an email message
        msg = email.message_from_string(eml_content)

        # Print the subject of the email
        subject = msg["Subject"]
        if subject:
            print("Subject:", subject)
        else:
            print("No subject found.")

        # Print the sender of the email
        sender = msg["From"]
        if sender:
            print("From:", sender)
        else:
            print("No sender found.")

        # Print the recipients of the email
        recipients = msg["To"]
        if recipients:
            print("To:", recipients)
        else:
            print("No recipients found.")

        # Extract the body of the email
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                if body:
                    print("Body:", body.decode())
                else:
                    print("No payload found for this part")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python eml_to_email_message.py <base64_encoded_eml_file>")
        sys.exit()
    file_path = sys.argv[1]

    # Decode the base64-encoded .eml file
    with open(file_path, "rb") as f:
        base64_content = f.read()
    eml_content = base64.b64decode(base64_content)

    # Save the decoded .eml content as a .eml file
    with open("decoded_eml.eml", "wb") as f:
        f.write(eml_content)

    # Run the convert_eml_to_email_message function on the decoded .eml file
    convert_eml_to_email_message("decoded_eml.eml")
