# Version 1

import datetime as dt
import pandas as pd
import smtplib
import random


def congratulations(name, letter_id=1, address=None):
    MY_EMAIL = 'YOUR EMAIL'
    MY_PASSWORD = 'YOUR PASSWORD'

    with open(f'letter_templates/letter_{letter_id}.txt', 'r') as file:
        name_for_letter = file.read()
    content = name_for_letter.replace('[NAME]', name)
    # Email
    with smtplib.SMTP('YOUR EMAIL PROVIDER SMTP SERVER ADDRESS') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= address,
                            msg=f"Subject:Happy Birthday!\n\n{content}")

# Date
now = dt.datetime.now()
MONTH = now.month
DAY = now.day
print(MONTH)
# Database birthday
data = pd.read_csv("birthdays.csv")
birthday_date = data.to_dict(orient="records")

for d in range(len(birthday_date)):
    if birthday_date[d]['month'] == MONTH and birthday_date[d]['day']:
        rn = random.randint(1, 3)
        names = birthday_date[d]['name']
        address = birthday_date[d]["email"]
        congratulations(names, rn, address)
# Version 2


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
