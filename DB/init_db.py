import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Replace the values for each INSERT INTO statement as desired
cur.execute("INSERT INTO user (username, password, firstname, lastname, email, gender, role, phone, dob, height_cm, weight_kg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('newadmin', 'newpass', 'NewAdminFirstName', 'NewAdminLastName', 'newadmin@example.com', 'male', 'admin', '9999999999', '1990-1-1', 180, 70))

cur.execute("INSERT INTO user (username, password, firstname, lastname, email, role, phone, dob, height_cm, weight_kg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('newuser1', 'pass1', 'FirstName1', 'LastName1', 'newuser1@example.com', 'doctor', '7777777777', '1991-1-1', 165, 60))

cur.execute("INSERT INTO user (username, password, firstname, lastname, email, role, phone, dob, height_cm, weight_kg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('newuser2', 'pass2', 'FirstName2', 'LastName2', 'newuser2@example.com', 'nurse', '6666666666', '1992-2-2', 160, 50))

cur.execute("INSERT INTO device (data_type, measurement, patient_name, doctor_name, nurse_name) VALUES (?, ?, ?, ?, ?)",
            ('blood_pressure', '120/80', 'newuser2', 'newuser1', 'newuser2'))

cur.execute("INSERT INTO chat (sender, recipient, type, content) VALUES (?, ?, ?, ?)",
            ('newuser1', 'newuser2', 'message', 'Hello, how can I help you?'))

cur.execute("INSERT INTO appointment (doctor_name, patient_name, appointment_date, start, finish, symptom) values (?, ?, ?, ?, ?, ?)",
            ('DrNewUser1', 'NewUser2', '2023-10-10', '10:00:00', '11:00:00', 'general_checkup'))

connection.commit()
connection.close()
