# Birthday Email Sender (Python)

This project is a Python automation script that sends a **personalized birthday email** to people listed in a CSV file.
The script checks if today matches any birthday in the dataset and automatically sends a randomly selected birthday message.

## Features

* Reads birthday data from a CSV file using **pandas**
* Checks if today's date matches any birthday
* Randomly selects a birthday message template
* Replaces `[NAME]` in the template with the person's actual name
* Sends a personalized email using **SMTP**

## Technologies Used

* Python
* pandas
* smtplib
* datetime
* random

## Project Structure

```
birthday-email-sender/
│
├── main.py
├── birthdays.csv
├── README.md
│
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## birthdays.csv Format

The CSV file must contain the following columns:

```
name,email,year,month,day
John,john@email.com,1995,3,15
Emma,emma@email.com,1998,7,21
```

* **name** – Person's name
* **email** – Email address where the birthday message will be sent
* **year** – Birth year (not required for the script but can be included)
* **month** – Birth month
* **day** – Birth day

## Letter Templates

Inside the `letter_templates` folder, create text files containing birthday messages.

Example:

```
Happy Birthday [NAME]!

Wishing you a wonderful day filled with happiness and success.

Best wishes,
Your Friend
```

The script will automatically replace `[NAME]` with the person's actual name.

## How It Works

1. The script reads `birthdays.csv`.
2. It checks if today's **month and day** match any record in the dataset.
3. If a match is found:

   * A random letter template is selected.
   * `[NAME]` is replaced with the person's name.
4. The script sends the email through Gmail's SMTP server.

## Setup

### 1. Install Dependencies

```
pip install pandas
```

### 2. Enable Gmail App Password

For security reasons, Gmail requires an **App Password** instead of your regular password.

Steps:

1. Enable **2-Step Verification** on your Google account.
2. Generate an **App Password**.
3. Use that password in the script.

Example:

```python
user_email = "your_email@gmail.com"
user_password = "your_app_password"
```

### 3. Run the Script

```
python main.py
```

## Example Output

If today matches someone's birthday, the script will send them a personalized birthday email automatically.

## Security Note

Do **not** upload your real email password to GitHub.
Instead, store sensitive information using **environment variables** or a `.env` file.

## Future Improvements

* Use environment variables for email credentials
* Add logging
* Schedule the script to run daily using **cron** or **Task Scheduler**
* Add HTML email templates
* Deploy the script on a cloud server

## Author

Abu Hurayra Farhan
