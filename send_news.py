import smtplib, ssl, os
from req import get_data

def create_mail_content(keyword):
    data = get_data(keyword)
    message = "subject: Daily News by Python\n"
    for article in data[:20]:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        message += f"{title}\n{description}\nFull article: {url}\n\n"
        # if (title and description and url):
        #     message += f"Title: {title}\nDescription: {description}\nFull article: {url}\n"
    return message

def send_news(reciever, message):
    host = "smtp.gmail.com"
    port = 465
    username = "py.defaultsender0@gmail.com"
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message.encode("utf-8"))
