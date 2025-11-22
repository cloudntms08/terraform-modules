from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS

# Database configuration
db_config = {
    'host': '10.0.0.4',  # Database VM IP
    'user': 'enquiry_user',
    'password': 'EnquiryPassword123!',
    'database': 'enquiries_db'
}

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        message = data['message']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO inquiries (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify(success="Inquiry submitted successfully.")

    except Exception as e:
        print("Error:", e)
        return jsonify(error="Failed to connect to the database."), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
