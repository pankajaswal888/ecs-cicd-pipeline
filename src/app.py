import os
from flask import Flask, request
import logging

app = Flask(__name__)

# Configuration
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
PORT = int(os.getenv('PORT', '8000'))

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    logger.info("Data endpoint accessed")
    return jsonify({"data": [1, 2, 3]})

@app.route('/api/process', methods=['POST'])
def process_data():
    req_data = request.get_json()
    logger.info(f"Processing: {req_data}")
    return jsonify({"received": req_data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
