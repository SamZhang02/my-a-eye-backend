from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from functions.conversation import get_conversation_response
import os

load_dotenv()

UPLOAD_FOLDER = 'recs'

app = Flask(__name__)

CORS(app)

@app.route('/')
def default():
  return jsonify({'message': 'Hello, World!'})

@app.route('/api/eye', methods=['POST'])
def respond_conversation():

  try:
    past_messages = request.json['pastMessages']
    current_message = request.json['currentMessage']
    images = request.json['images']
  except Exception as err:
    print(err)
    return jsonify({'message': 'Error!', 'error': str(err)}), 400

  res, err = get_conversation_response(
    images, current_message, prior_conversation=past_messages
  )

  if err:
    return jsonify({'message': 'Error!', 'error': str(err)}), 400

  return jsonify({'message': res})

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/record', methods=['POST'])
def record_audio():
  try:
    audio = request.files['audio']
    response_data = {'message': 'Data received successfully', 'audio': audio}
    # print(response_data)

    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'recording.wav')
    audio.save(filename)

    return response_data['message']

  except Exception as e:
    return jsonify({'error': str(e)}), 400

#
# Run the app if this file is executed directly
if __name__ == '__main__':
  app.run(debug=True)
