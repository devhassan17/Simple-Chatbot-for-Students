import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

genai.configure(api_key='AIzaSyCyHZ07xZqI5e1tA6_KV2sIfWDNm7_a0oM')

model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']

    # chat = model.start_chat(history=[])
    # response = chat.send_message(user_input)

    response = model.generate_content(f' response very shortly, wisely, full-fill all commands for this message.Write text without headings.Just give information in paragraph {user_input}')

    return jsonify(content=response.text)

if __name__ == '__main__':
    app.run(debug=True)