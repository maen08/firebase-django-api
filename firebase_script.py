import pyrebase


config = {
  "apiKey": "AIzaSyAwc_TM-Gq2XbwgupZxQiQvvduJKxLctiQ",
  "authDomain": "maen-try-firebase.firebaseapp.com",
  "databaseURL": "https://maen-try-firebase-default-rtdb.firebaseio.com",
  "projectId": "maen-try-firebase",
  "storageBucket": "maen-try-firebase.appspot.com",
  "messagingSenderId": "347874418875",
  "appId": "1:347874418875:web:e892faecd4b3555295899e",
  "measurementId": "G-W02B31G0D5"

}





# initialisatiing pyrebase
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()

# selecting the column in the database
check = db.child("users")

try:
    data = {"name": "Stan"}
    db.child("users").push(data)

    print('DB WELL WRITTEN')

except:
    print('ACCESS DENIED')

# print(check)