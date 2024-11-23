import imaplib

def clean_emails(username, password, sender):
    try:
        # Connect to the server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)

        # Select the inbox
        mail.select("inbox")

        # Search for emails from the sender
        status, messages = mail.search(None, f'(FROM "{sender}")')

        if status == "OK" and messages[0]:
            email_ids = messages[0].split()
            for msg_id in email_ids:
                mail.store(msg_id, '+FLAGS', '\\Deleted')

            mail.expunge()  # Permanently delete marked emails
            return f"Emails from '{sender}' have been deleted!"
        else:
            return f"No emails found from '{sender}'."

        # Close the connection
        mail.close()
        mail.logout()

    except Exception as e:
        return f"An error occurred: {e}"