from reschpc import auth
from reschpc import info

TOKEN = "YOUR_TOKEN"           # <------
myauth = auth.Auth(TOKEN)

print("Info on 'Analyses'::") 
info.getinfo(myauth,0)

print("Info on 'Core Types'::")
info.getinfo(myauth,1)
