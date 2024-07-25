import smtplib
import datetime as dt
import random

email = input("SENDER EMAIL: ")
password = input("SENDER PASSWORD: ")
receiver_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)    



text = f"Subject: Monday Motivation\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, password)

server.sendmail(email, receiver_email, text)
