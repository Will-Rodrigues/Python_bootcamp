from flask import Flask, render_template, request
import smtplib as smtp

app = Flask(__name__)

EMAIL = ''
PASS = ''


@app.route('/')
def home():
    return render_template('contact.html')


@app.route('/submit-email', methods=['POST'])
def submit_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    with smtp.SMTP("smtp.office365.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject:New Blog Message\n\nfrom:{name}\nemail:{email}\nphone:{phone}\nmessage:{message}")
    return 'message send'


if __name__ == '__main__':
    app.run(debug=True)
