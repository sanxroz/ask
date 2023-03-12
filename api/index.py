from flask import Flask, render_template, request, jsonify
import requests
import openai

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('./home.html')


@app.route('/submit', methods=['POST'])
def submit():

    open_ai_cookie = request.cookies.get("not-api-cookie")

    if not open_ai_cookie:
        return jsonify({'message': 'No OpenAI key, check https://platform.openai.com/account/api-keys for your key'})
    else:
        try:
            openai.api_key = f"{open_ai_cookie}"
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{request.json['inputValue']}"}])
            return jsonify({'message': completion.choices[0].message.content})
        except requests.exceptions.RequestException as err:
            print('Something went wrong:', err)
            return jsonify({'message': 'Something went wrong'}), 500


if __name__ == '__main__':
    app.run(debug=True)
