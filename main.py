##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random
import datetime as dt

now = dt.datetime.now()
today = dt.date.today()
current_day = today.day
current_month = now.month

user_email = "alansnap229@gmail.com"
user_password = "zrju wepy gfke wnvw"

bday_email = ""
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

chosen_file = random.choice(letters)

# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')


# 2. Check if today matches a birthday in the birthdays.csv
for index, row in data.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        bday_email = row["email"]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


        with open(f"letter_templates/{chosen_file}", "r") as file:
            content = file.read()
            modified_content = content.replace("[NAME]", row["name"])
            print(modified_content)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user_email, password=user_password)
            connection.sendmail(from_addr=user_email,to_addrs=bday_email,msg=f"Subject:happy birthday!\n\n{modified_content}")