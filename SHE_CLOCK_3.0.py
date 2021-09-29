from plyer import notification
from text_to_speech import speak
import datetime


def welcome_msg():
    return ('''
        Welcome to SHE_CLOCK_3.0!!!
    Your Personalised Desktop Notifier is Here...
    ''')


def instructions():
    instruction = ('''
    SHE_CLOCK_3.0
    -------------
    Instructions

    >>> Your SHE_CLOCK_3.0 is in 12 hour format.
    >>> Initially, Set your time in hour.
    >>> Then, Set your time in minute.
    >>> Select am or pm?
    >>> Now you can set your remainder
    >>> and, Add more details, if any
    >>> for example- 
      > Hour : 10
      > Minute : 38
      > am or pm? pm
        Your alarm is set to 10:38 pm
      > Your reminder please: It's bed time.
      > More to add-on: Don't forget to drink water. 

    Let's Start the journey!!!
    --------------------------''')
    return instruction


def notifier():
    alarm_hour = int(input("Hour : "))
    alarm_minute = int(input("Minute : "))
    am_pm = str(input("am or pm?"))

    print("Your alarm is set to ", alarm_hour, ":", alarm_minute, am_pm)
    title = input("Your reminder please: ")
    message = input("More to add-on: ")

    if am_pm == "pm":
        alarm_hour += 12

    while 1 == 1:
        if (alarm_hour == datetime.datetime.now().hour) and (alarm_minute == datetime.datetime.now().minute):
            print("Time for your alarm")
            print(datetime.datetime.now())
            speak(title, "en", save = True, file = "schedule.mp3")
            return notification.notify(
                app_name = "SHE_CLOCK_3.0",
                title = title,
                message = message,
                app_icon = "myclock.ico",
                timeout = 20,)


def she_clock():
    print(welcome_msg())
    instructn = input("Do you want to know more? (yes/no)")
    if instructn.lower() == "yes":
        print(instructions())
    print('''
        *** Let's GO ***
    *** Set your Time Now *** ''')
    return notifier()


she_clock()