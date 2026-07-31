from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_age():
    birthdate_str = request.form['birthdate']
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(month=birthdate.month + 1) - birthdate).days
    
    if months < 0:
        years -= 1
        months += 12

    return render_template('index.html', years=years, months=months, days=days)

if __name__ == '__main__':
    app.run(debug=True)
