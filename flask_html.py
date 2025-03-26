from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5007)


# This ^ originally said the code below. Made it correct and made the port (5007) 

"""
if __name__ == '__main__':
    app.run(debug=True)
"""