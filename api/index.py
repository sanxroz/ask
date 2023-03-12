from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('./home.html')


@app.route('/submit', methods=['POST'])
def submit():

    open_ai_cookie = request.cookies.get("not-api-cookie")

    openai.api_key = f"{open_ai_cookie}"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{request.json['inputValue']}"}])
    return jsonify({'message': completion.choices[0].message.content})


if __name__ == '__main__':
    app.run(debug=True)
