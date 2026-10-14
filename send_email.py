import smtplib , ssl

host = "smtp.gmail.com"
port = 465

username = "mehrbod.amin90@gmail.com"
password = "bfxi fgeb esdd ooig"

receiver_email = "mehrbod.amin90@gmail.com"
context = ssl.create_default_context()

message = """Hi!
How are you?
good bye :)"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver_email , message)