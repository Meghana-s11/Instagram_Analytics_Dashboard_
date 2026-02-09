from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

VALID_CODES = {
    "STU123": "student",
    "ADM999": "admin"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form['access_code']
        role = request.form['role']

        if code in VALID_CODES and VALID_CODES[code] == role:
            session['user'] = role
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid Access Code")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/forgot')
def forgot():
    return render_template('forgot.html')
