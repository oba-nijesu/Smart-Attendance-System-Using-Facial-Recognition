import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://smartfacialrecogattendance-default-rtdb.firebaseio.com/"
})

# Reference to the "Students" node in Firebase
ref = db.reference('Students')

# Student data
data = {
    "2101944": {
        "name": "Obanijesu Adeyemo",
        "major": "Physics",
        "starting_year": 2021,
        "reg_number": 2101944,
        "total_attendance": 11,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2100023": {
        "name": "Adegoke Boluwatife",
        "major": "Accounting",
        "starting_year": 2021,
        "reg_number": 2100023,
        "total_attendance": 10,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2203145": {
        "name": "Triumph-Igurube Oreva",
        "major": "Economics",
        "starting_year": 2022,
        "reg_number": 2203145,
        "total_attendance": 7,
        "level": 300,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "2100971": {
        "name": "Chukwunenye Somto",
        "major": "Physics",
        "starting_year": "2021",
        "reg_number": 2100971,
        "total_attendance": 0,
        "level": 400,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Insert data into Firebase
for key, value in data.items():
    ref.child(key).set(value)

