from skpy import Skype
import os.path

slogin = Skype("email@gmail.com","password")

contact = slogin.contacts["live:.id"] #live id detail of a person
with open ("","rb") as f:  #path of the image file with
    contact.chat.sendFile(f,"filename here",image = True) 

#group creation
group = slogin.chats.create(["",""]) #place the live id of the persons you have to add in the group
#sending messages for a particular person
contact = slogin.contacts["live:.id"] #lib=ve id detail of a person
contact.chat.sendMsg("welcome to the chat")

#for i in contact:
 #   print(i)