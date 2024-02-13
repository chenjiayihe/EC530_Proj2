from flask import Flask, request, jsonify
app = Flask(__name__)

# Dummy data stores for demonstration purposes
users = []
device_makers = []
appointments = []
messages = []
patient_devices = []
patient_measurements = []
alerts = []

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = len(users) + 1
    data['userId'] = user_id
    users.append(data)
    return jsonify(data), 201

@app.route('/api/users/<int:user_id>/roles', methods=['PATCH'])
def assign_change_roles(user_id):
    data = request.json
    for user in users:
        if user['userId'] == user_id:
            user['roles'] = data['roles']
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/api/deviceMakers', methods=['POST'])
def register_device_maker():
    data = request.json
    maker_id = len(device_makers) + 1
    data['makerId'] = maker_id
    device_makers.append(data)
    return jsonify(data), 201

@app.route('/api/deviceMakers/<int:maker_id>/status', methods=['PATCH'])
def enable_disable_device_maker(maker_id):
    data = request.json
    for maker in device_makers:
        if maker['makerId'] == maker_id:
            maker['status'] = data['status']
            return jsonify(maker), 200
    return jsonify({"error": "Device maker not found"}), 404

@app.route('/api/patients/<int:patient_id>/devices', methods=['POST'])
def assign_device_to_patient(patient_id):
    data = request.json
    data['patientId'] = patient_id
    patient_devices.append(data)
    return jsonify(data), 200

@app.route('/api/patients/<int:patient_id>/measurements', methods=['POST'])
def record_measurement(patient_id):
    data = request.json
    data['patientId'] = patient_id
    patient_measurements.append(data)
    return jsonify(data), 201

@app.route('/api/patients/<int:patient_id>/alerts', methods=['POST'])
def set_measurement_alert(patient_id):
    data = request.json
    data['patientId'] = patient_id
    alerts.append(data)
    return jsonify(data), 201

@app.route('/api/appointments', methods=['POST'])
def schedule_appointment():
    data = request.json
    appointment_id = len(appointments) + 1
    data['appointmentId'] = appointment_id
    appointments.append(data)
    return jsonify(data), 201

@app.route('/api/messages', methods=['POST'])
def send_message():
    data = request.json
    message_id = len(messages) + 1
    data['messageId'] = message_id
    messages.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
