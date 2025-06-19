from flask import Flask, render_template, request, jsonify
from cipher import caesar, railfence, playfair, vigenere

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt/<cipher_name>', methods=['POST'])
def encrypt(cipher_name):
    data = request.json
    text = data.get('text', '')
    key = data.get('key', '')

    result = ''
    if cipher_name == 'caesar':
        result = caesar.encrypt(text, int(key))
    elif cipher_name == 'railfence':
        result = railfence.encrypt(text, int(key))
    elif cipher_name == 'playfair':
        result = playfair.encrypt(text, key)
    elif cipher_name == 'vigenere':
        result = vigenere.encrypt(text, key)
    else:
        return jsonify({'error': 'Unknown cipher'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
