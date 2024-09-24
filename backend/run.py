import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # This loads the .env file

# Use environment variables
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
CORS_ORIGIN = os.environ.get('CORS_ORIGIN', '*')

# Create the Flask app
app = Flask(__name__)

# Setup CORS
CORS(app, resources={r"/*": {"origins": CORS_ORIGIN}}, supports_credentials=True)

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins=CORS_ORIGIN, allow_credentials=True)

# Import and register your routes and events here
# from app.routes import ...
# from app.events import ...

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    socketio.run(app, host='0.0.0.0', port=port, debug=DEBUG)