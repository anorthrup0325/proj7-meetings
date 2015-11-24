"""
Configuration of 'Meetings' Flask app. 
Edit to fit development or deployment environment.

"""
import random 

### My local development environment
#PORT=5000
#DEBUG = True
#GOOGLE_LICENSE_KEY = ".client_secret.json"

### On ix.cs.uoregon.edu (Michal Young's instance of MongoDB)
PORT=5280
DEBUG = False # Because it's unsafe to run outside localhost
MONGO_URL = "mongodb://editor:simon_pegg@localhost:4941/memos" # On ix
GOOGLE_LICENSE_KEY = ".goog_app_key.json"
HOST = "0.0.0.0"
