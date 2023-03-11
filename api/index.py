from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('./home.html')


@app.route('/submit', methods=['POST'])
def submit():
    url = 'https://bing.khanh.lol/completion'
    headers = {'Content-Type': 'application/json'}
    data = {'prompt': request.json['inputValue'], 'includeDetails': True}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()['details']['spokenText'].strip()
        return jsonify({'message': result})
    except requests.exceptions.RequestException as err:
        print('Something went wrong:', err)
        return jsonify({'message': 'Something went wrong'}), 500


if __name__ == '__main__':
    app.run(debug=True)
