from flask import Flask, render_template,request

app = Flask(__name__)

def gpt3(input):
    return "This is GPT3. I got your input " + input

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/getResult', methods=['POST'])
def getOutput():
    ...

    input = (request.form['input'])
    output = gpt3(input)

    return render_template('output.html',output = output)


if __name__ == '__main__':
    app.run()

