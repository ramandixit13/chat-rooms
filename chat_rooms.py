#!/usr/bin/env python
# coding: utf-8

# ## Chat Rooms
# You have been pretty disappointed at the current quality of chat room applications and vow to create your own, start up a new Internet company, obtain venture capital funding, integrate advertisement into your chat program, quintuple revenues in a six-month period, go public, and retire. However, none of this will happen if you do not have a pretty cool chat application.
# 
# ### There are three classes you will need: 
# - A Message class containing a message string and any additional information such as broadcast or single recipient
# - A User class that contains all the information for a person entering your chat rooms
# - A Room class that represents a more sophisticated chat system where users can create separate "rooms" within the chat area and invite others to join

# In[96]:


import uuid
from datetime import datetime

# User Classes
class User():
    def __init__(self,userID,username):
        self.userID = userID
        self.username = username
        self.groupsJoined = []
        self.admin = False
    
    def sendDirectMessage(self):
        sender = self.username
        recipient = input("Who do you want to send the message to?")
        for user in users:
            if recipient == user.username:
                messageContent = input("Enter your message.")
                print("Sending message to %s..." %(recipient))
                message = Single(messageContent,sender, recipient)
                messages.append(message)
                return message
        print("User doesn't exist")
    
    def sendBroadcastMessage(self):
        sender = self.username
        recipient = input("Which chat room do you want to send the message to?")
        for room in rooms:
            if recipient == room.roomName:
                if sender in room.roomMembers:  
                    messageContent = input("Enter your message.")
                    print("Sending message to %s..." %(recipient))
                    message = Broadcast(messageContent,sender,room)
                    messages.append(message)
                    return message
                print("You're not in the group")
                return
        print("Chat Room doesn't exist")    
    
    def createRoom(self):
        roomName = input("Hello Admin. What would you like the chat room to be named?")
        room = Room(roomName,self)
        rooms.append(room)
        return room  
    
    def __repr__(self):
        return "(User ID: %s, Username: %s)" %(self.userID, self.username)

# Admin that creates users
class Admin(User):
    def __init__(self,userID,username):
        User.__init__(self, userID,username)
        self.admin = True
    
    def createUser(self):
        userID = users[-1].userID + 1
        username = input("What's the username?")
        user = User(userID,username)
        users.append(user)
        return user

                
# Message Classes
class Message:
    def __init__(self,messageContent,sender):
        self.messageContent = messageContent
        self.sender = sender
        self.createdAt = datetime.now()

class Single(Message):
    def __init__(self,messageContent,sender, recipientName):
        super().__init__(messageContent, sender)
        self.recipientName = recipientName
        self.typeOfMessage = "single"    

    def __repr__(self):
            return "Sent At: %s, Sent By: %s, Sent To: %s, Message: %s, Type: %s" %(self.createdAt,self.sender,self.recipientName, self.messageContent, self.typeOfMessage)        
        
class Broadcast(Message):
    def __init__(self,messageContent,sender, chatRoomRecipient):
        super().__init__(messageContent, sender)
        self.chatRoom = chatRoomRecipient.roomName
        self.typeOfMessage = "broadcast"
        
    def __repr__(self):
            return "Sent At: %s, Sent By: %s, Sent To: %s, Message: %s, Type: %s" %(self.createdAt,self.sender,self.chatRoom, self.messageContent, self.typeOfMessage)  

# Room Classes
class Room:
    def __init__(self,roomName, user):
        self.admin = user.username
        self.roomName = roomName
        self.roomID = uuid.uuid1()
        self.roomMembers = [user.username]
    
    def addMembers(self):
        username = input("What's your username?")
        if username == self.admin:
            print("You are an admin. Adding the members")
            membersToAdd = input("Enter the users separated by commas and a space (name1, name2, etc.)").split(", ")
            for member in membersToAdd:
                self.roomMembers.append(member)
        else:
            print("You are not an admin of the group. You can't invite members to a room.")        


# In[97]:


admin = Admin(0,'admin')        
users = [admin]
messages = []
rooms = []   


# In[98]:


raman = admin.createUser()
dylan = admin.createUser()
# deepika = admin.createUser()


# In[99]:


tennis = admin.createRoom()
basketball = admin.createRoom()
football = admin.createRoom()


# In[100]:


tennis.addMembers()


# In[101]:


tennis.roomMembers


# In[102]:


raman.createRoom()


# In[79]:




