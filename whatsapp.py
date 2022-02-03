import pywhatkit
print("Enter mobile Number")
mobile_no=input()
print("Enter Message")
msg=input()
print("Enter time")
hh=int(input())
mm=int(input())


# Send a WhatsApp Message to a Contact at 1:30 PM
# for i in range(60):

pywhatkit.sendwhatmsg(mobile_no, msg, hh,mm )
