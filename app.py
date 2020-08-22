# app.py
import os
import json
import requests

from flask import Flask, render_template,request

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
DAVINCI_URL = "https://api.openai.com/v1/engines/davinci/completions"

headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer {}".format(API_KEY)
}

payload = {
	"max_tokens": 60,
	"temperature": 0,
	"top_p": 1,
	"n": 1,
	"stream": False,
	"logprobs": None,
	"stop": "\n"
}

def gpt3(input):
	payload['prompt'] = input
	response = requests.post(DAVINCI_URL, headers=headers, data=json.dumps(payload))
	res_data = response.json()
	output = res_data['choices'][0]['text'].strip()
	return output

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/getResult', methods=['POST'])
def getOutput():
	input = (request.form['input'])
	output = gpt3(input)

	return render_template('output.html',output = output)


if __name__ == '__main__':
	app.run()
