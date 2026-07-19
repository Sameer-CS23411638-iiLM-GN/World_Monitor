from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
    location = request.args.get('location', 'world')
    data = {
        'status': 'online',
        'location': location,
        'message': f'World Monitor is tracking {location}.',
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
