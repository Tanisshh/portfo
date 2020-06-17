from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return 'thanks'
        except:
            return 'sorry, did not save to database'
    else:
        return 'something wrong'


def write_csv(data):
    with open('database.csv', mode='a', newline='') as csvfile:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([name, email, message])
