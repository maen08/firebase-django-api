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


# push data
data = {"name": "johnd", "age": 104}

db.push(data)  # push to db with auto generated key by firebase


# generate your own key
db.child('example').set(data)