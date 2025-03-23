from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Dockerized Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# lines 1 & 9 were commented out for some reason
# line 10 was missing the = sign for the port number & I had to change the IP from 'x.0.0.0' to '0.0.0.0'