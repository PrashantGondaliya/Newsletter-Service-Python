#Program to let user Subscribe or Unsubscribe
#Using Pandas we will edit the excel sheet of Subscribers
import pandas as pd
import smtplib
import time

df = pd.read_excel(r"C:\Users\prash\Desktop\Web Designing\Subscribers.xlsx")

def action():
    print("1. Subscribe to our service")
    print("")
    print("2. Unsubscribe")
    print("")

    res = int(input("Select any of the above Feature"))

    if res == 1:
        print("Glad to know that you are interested in our News Service")
        time.sleep(1)
        print("Subscribing is made way too easy, we just need two of your details")
        time.sleep(1)
        name = input("please enter your Full Name here : ")
        print("oh hello there, Nice to see you " + name)
        time.sleep(1)
        print("We now only need your Email address on which you would like to receive our service")
        print("Make sure you enter your email correctly")
        email = input("Please enter your email address here : ")
        print("That's it, you would now had received an confirmation email on " + email + "")

        #Sending an confirmation Email using smtplib
        subscriber = email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login("jc107405@gmail.com","ebszeynzcegoogtz")
        msg = "Welcome on board, So this email is the confirmation that you have successfully subscribed to our news servi1ce.\n Hope you find it fun and useful.\n Thank you."
        subject = "Subscription Conformation"
        body = "Subject: {}\n\n{}".format(subject,msg)
        server.sendmail("jc107405@gmail.com", subscriber, body)
        server.quit()
        
action()