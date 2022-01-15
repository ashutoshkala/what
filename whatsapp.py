import pywhatkit
print("Enter mobile Number")
mo=input()
print("Enter Message")
x=input()
print("Enter time")
hh=int(input())
mm=int(input())


# Send a WhatsApp Message to a Contact at 1:30 PM
# for i in range(60):

pywhatkit.sendwhatmsg(mo, x, hh,mm )
