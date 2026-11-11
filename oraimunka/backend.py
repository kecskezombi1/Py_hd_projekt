from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/api/uzenet')
def uzenet():
    return jsonify({'uzenet': 'sikerült'})


app.run(port=5000)