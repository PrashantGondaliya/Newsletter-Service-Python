#NEWS LETTER
from re import X
#importing pandas to connect and access the subscribers' list(excel sheet)
import pandas as pd
#importing smtplib library to send emails to the subscribers
import smtplib 

x = pd.read_excel(r'C:\Users\prash\Desktop\Web Designing\Subscribers.xlsx')
subscribers = x['Emails'].values
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login("jc107405@gmail.com","ebszeynzcegoogtz")
msg = "yess!! if you are reading this then i finally made the basic working news service program Peace "
subject = "so i did it ??"
body = "Subject: {}\n\n{}".format(subject,msg)
for subscriber in subscribers:
    server.sendmail("jc107405@gmail.com", subscriber, body)
server.quit()
#print(emails)