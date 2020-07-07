from reschpc import auth

TOKEN = "YOUR_TOKEN"           # <-----
PROJECTID = "YOUR PROJECT_ID"  # <-----
myauth = auth.Auth(TOKEN,PROJECTID)

print(f"  Authentication Info::\n  {myauth}")
