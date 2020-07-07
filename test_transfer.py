from reschpc import auth
from reschpc import transfer as tf

TOKEN = "YOUR_TOKEN"                  # <----
PROJECTID = "YOUR_PROJECT_ID"         # <----
myauth = auth.Auth(TOKEN,PROJECTID)

FILENAME="../data/input.zip"
zipfile_id = tf.Transfer.upload(myauth, FILENAME)
print(f"  Zip file id:'{zipfile_id}'")

