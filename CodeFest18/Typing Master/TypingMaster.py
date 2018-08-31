from pwn import *

#Connect to to server
conn = remote('34.216.132.109', 9093)

#Get the text
text = conn.recv()

#Parse text to get the first letter
firstLetter = text.find('\'') + 1

#Cut the text and parse it to get the second letter
cutText = text[firstLetter + 2:]
secondLetter = cutText.find('\'') + 1

#Parse text to get the numbers to multiply letters
numbersInText = [int(s) for s in text.split() if s.isdigit()]

#Construct String to give program to get the flag
StringToSend = str(text[firstLetter]) * numbersInText[0]
StringToSend = StringToSend + str(cutText[secondLetter]) * numbersInText[1]
StringToSend = StringToSend + str(ord(text[firstLetter]) + ord(cutText[secondLetter]))

#PAYLOAD DEPLOYMENT -- EMBRACE
conn.sendline(StringToSend)

#Receive flagz
print(conn.recvline(timeout=3))
