from flask import Flask, jsonify
from flask_cors import CORS

UPLOAD_FOLDER = 'recs'

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS
CORS(app)

# Define a route for the default URL, which returns a JSON response
@app.route('/api')
def default():
    return jsonify({'message': 'Hello, World!'})

# Define a route for the default URL, which returns a JSON response
@app.route('/api/eye')
def eye():
    return jsonify(
        {'message': 'You have reached the correct endpoint!'}
    )


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
