from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from functions.conversation import get_conversation_response, get_transcription
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
  body = request.json 

  past_messages = body.get('pastMessages') # type: ignore
  current_message = body.get('currentMessage') # type: ignore
  images = body.get('images') # type: ignore

  res, err = get_conversation_response(
    images, current_message, prior_conversation=past_messages
  )

  if err:
    return jsonify({'message': 'Error!', 'error': str(err)}), 400

  return jsonify({'message': res})

@app.route('/s2t', methods=['POST'])
def speech2text():
  body = request.json

  base64_audio = body.get('audio') #type: ignore

  message, err = get_transcription(base64_audio)

  if err:
    return jsonify({'message': 'Error!', 'error': str(err)}), 400
  
  return jsonify({'message': message})

if __name__ == '__main__':
  app.run(debug=True)
