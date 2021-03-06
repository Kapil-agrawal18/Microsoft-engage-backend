import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "tanmay.mohanty18112002@gmail.com"
APP_PASSWORD = "srtnvgnphangdzvn"

def emailRecords(recipient_email, no_criminals, csv_file):
    msg = EmailMessage()
    msg['Subject'] = "Video Processing Complete | Check Results"
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(
        "Greetings!\nYour video has been processed.\nWe found " + str(no_criminals) + " criminal instances in this Video.\nKindly find the attached CSV file to keep the record of timestamps.\nRegards,\nFaceX")

    with open(csv_file, 'rb') as f:
        file_data = f.read()

    msg.add_attachment(file_data, maintype="application", subtype="csv", filename='Criminal_Records.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)


# emailRecords('kunal10061994@gmail.com', 'Video Processed!', 'Hi there, something is attached', r'myproject\myapi\test.csv')