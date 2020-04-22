Download chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
Make sure it is compatible with your browser.
Place chromedriver executable in the project directory.

Install selenium:

    pip install selenium

Create an empty directory <chrome_profile> in the project directory. Chrome profile data goes here, populated when run.

Create a <creds.py> file in your project directory.
Enter static values here.

    email = "hrstop email"
    password = "hrstop password"
    time_of_login = enter time in "%H:%M"
    time_of_logout = format as a string
    last_time_of_login = enter time in "%H:%M"
    last_time_of_logout = format as a string


Scheduling the CRON

On terminal: 

    env EDITOR=nano crontab -e

Enter following in nano editor:

    58 9 * 4-5 1-6 /path/to/python /path/to/script.py
    11 19 * 4-5 1-6 /path/to/python /path/to/script.py
    minute hour day month(April-May) day_of_week(Mon-Sat) /path/to/python /path/to/script.py
