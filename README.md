# Phishing-Attack-Simulation

# Phishing Attack Simulation

This project simulates a phishing attack and provides educational insights into how phishing works. The application is built using Flask, and its purpose is to showcase a basic phishing website that mimics a login form.

---

## Features
- **Phishing Simulation**: Simulate a phishing attack by creating a login page that collects user information.
- **Form Submission**: Users can input their credentials into the phishing page, and the information is logged for analysis.
- **Flask Backend**: The server is built with Flask, and it captures the form data.

---

## Prerequisites
- Python 3.x
- Flask
- Internet connection (for access to the phishing page)

---

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies listed in `requirements.txt`.
4. Start the Flask server using `app.py`.
5. By default, the server runs on `http://127.0.0.1:5000`. Access the phishing page via this URL in your browser.

---

## Usage
1. Run the Flask server.
2. Open your browser and go to `http://127.0.0.1:5000`.
3. Use the phishing page to simulate login attempts by entering test credentials.
4. Check the server logs for submitted data.

---

## Phishing Page Example
1. Navigate to the phishing site in your browser.
2. Enter any test credentials (this is for educational purposes only).
3. The application logs the submitted credentials to analyze the phishing process.

---

## Project Structure
Phishing-Attack-Simulation/
- README.md  
- app.py: The main Flask app that handles server requests and form submissions.  
- fake_login.html: HTML template for the phishing page.  
- requirements.txt: Contains the Python dependencies for the project.  
- send_email.py: A script to send the captured credentials via email.  
- stolen_credentials.txt: Stores the captured credentials locally.

