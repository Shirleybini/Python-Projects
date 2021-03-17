
import smtplib
import random
import datetime as dt
import pandas as pd

my_email = "youremailid@email.com"
password = "your password"


now = dt.datetime.now()
today = (now.month,now.day)
 

birthdays = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row['month'],data_row['day']):data_row for (index, data_row) in birthdays.iterrows()}


if today in birthday_dict:
    N = random.randint(1,3)
    with open(f'letter_templates/letter_{N}.txt','r') as letter:
        Letter = letter.read()
    message = Letter.replace('[NAME]',birthday_dict[today][0])
    
    message = message.replace('Angela','Your Name')
    
    connection = smtplib.SMTP("smtp.gmail.com") #change according to email 
    connection.starttls()
    connection.login(user=my_email,password = password)
    connection.sendmail(from_addr=my_email,to_addrs=birthday_dict[today][1],msg= f"Subject:Happy Birthday!\n\n{message}")
    connection.close()



