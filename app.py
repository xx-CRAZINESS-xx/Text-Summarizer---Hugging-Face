from flask import Flask,render_template,request
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer xxxxxxx"}



def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/summarize",methods=['GET','POST'])
def summarize():
    if request.method == "POST":
        data = request.form["data"]
        max_length = int(request.form["max_length"])
        min_length = max_length // 4

        output = query({
            "inputs": data,
            "parameters": {"min_length": min_length, "max_length": max_length},
        })[0]

        output=str(list(output.values())[0])
        return render_template("index.html", result=output)
    else:
        return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)