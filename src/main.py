import pywhatkit as kit

phone_num = input("Enter receiver's mobile number (with country code): ")

message = "Hello, this message was sent using python automation."

hour = 19
minute = 21

kit.sendwhatmsg(phone_num, message, hour, minute)

print("Message Scheduled")
