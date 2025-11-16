import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
# password = input("Enter your password: ")
import getpass
password = getpass.getpass("Enter your password: ")
email = getpass.getpass("Enter your email: ")
smtp_object.login(email, password)
from_addr = email
to_addr = email
subject = input("Enter your subject: ")
message = input("Enter your message: ")
msg = f"Subject: {subject}\n\n{message}"
smtp_object.sendmail(from_addr, to_addr, msg)
smtp_object.quit()