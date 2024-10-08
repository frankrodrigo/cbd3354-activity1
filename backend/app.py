from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Database connection details
server = '34.44.131.30'
database = 'db1'
username = 'dbuser1'
password = 'dbuser1'

def get_db_connection():
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str)
    return conn

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    cellphone = data.get('cellphone')

    if not username or not cellphone:
        return jsonify({'error': 'Missing data'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, cellphone) VALUES (?, ?)", (username, cellphone))
        conn.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, cellphone FROM users")
        rows = cursor.fetchall()
        users = [{'username': row[0], 'cellphone': row[1]} for row in rows]
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
