from flask import Flask,jsonify
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBfNfIhkdvyVO7c03f3psbOh3WISC8B_Iw",
    "authDomain": "chat-476b0.firebaseapp.com",
    "databaseURL": "https://chat-476b0.firebaseio.com",
    "projectId": "chat-476b0",
    "storageBucket": "chat-476b0.appspot.com",
    "messagingSenderId": "862968309385",
    "appId": "1:862968309385:web:74c3ac1b8e144a13168858"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/",methods=['get'])
def home():
    db_events = db.child("clients").get().val()
    return jsonify(db_events)
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)