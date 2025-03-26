from flask import Flask, render_template, request, redirect, url_for, session
import random
# Line 2 ^ was commented out for some reason


app = Flask(__name__)
app.config.from_pyfile('config.py')
# Line 7 ^ was commented out for some reason



@app.route('/', methods=['GET', 'POST'])
def home():
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = None
    if request.method == 'POST':
        guess = int(request.form.get('guess', 0))
        session['attempts'] += 1

        if guess < session['target_number']:
            message = "Too low! Try again."
        elif guess > session['target_number']:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed it in {session['attempts']} attempts."
            session.pop('target_number', None)
            session.pop('attempts', None)

    return render_template('home.html', message=message)


if __name__ == '__main__':
    app.run()

# Line 35 was correct but commented out 
# Changed line 36 from what it was as shown in the below code: 

"""
if __name__ == "__main__": 
    app.run(debug=True) 
"""