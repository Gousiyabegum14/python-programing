#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket


# In[ ]:


s = socket.socket()
print("Sockets are created")
s


# In[ ]:


s.bind(('localhost',9999))
s.listen(3)
print("Waiting for connection")
while True:
    c.addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with client",addr,name)
    c.sent(bytes("welcom to python socket",utf-8))
    c.close


# In[ ]:


s = socket.socket()
print("socket created")
s.bind(('',1234))
s.listen(3) 
print("waiting for connections")
while True:
         c, addr = s.accept()
         name=c.recv(1024).decode()
print("connected with client", addr,name)
c.send(bytes("welcome to python socket".encode())) 
c.close()
break


# In[ ]:




