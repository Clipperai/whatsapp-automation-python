import pywhatkit as kit
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello Sir, Welcome to Whatsapp Automation tool!")

print("Hello Sir, Welcome to Whatsapp Automation tool!")

while(True):
    phone_num = input("Enter receiver's mobile number (with country code): ")

    message = input("Enter message to send: ")

    hour = int(input("Enter hour you want to send (1-12): "))

    minute = int(input("Enter minutes you want to send (0-59): "))

    period = input("AM or PM: ").upper()

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    kit.sendwhatmsg(phone_num, message, hour, minute)

    print("Message Sent Succesfully")

    choice = input("Do you want to use Whatsapp Automation tool again (yes/no): ").lower()
    if choice == "yes":
        continue
    else:
        break
