from flask import Flask

app = Flask(__name__)

@app.route("/") 
def home(): 
    return "<h1>Welcome to My Flask App!</h1> <p> This is a simple Flask application and only using flask.</p>"

"""
if __name__ == "__main__": 
    app.run(debug=True) 
^From the original code provided, commented out because we wanted to run the various scripts using 
port numbers instead as shown below. Same part was commented out of the flask and html default.py scripts
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5005)