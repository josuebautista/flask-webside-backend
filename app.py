from flask import Flask, jsonify, render_template

app = Flask(__name__)

jobs_list = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Mexico City, Mexico',
        'salary': '5000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Monterrey, Mexico',
        'salary': '5500',
    },
    {
        'id': 3,
        'title': 'Frontend Enginner',
        'location': 'Tijuana, Mexico',
        'salary': '6000',
    },
    {
        'id': 4,
        'title': 'Backend Enginner',
        'location': 'Mexico City, Mexico',
        'salary': '7000',
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs_list, company_name='My company name')


@app.route("/home", methods=['GET', 'POST'])
def home():
    return hello_world()

@app.route('/jobs')
def list_jobs():
    return jsonify(jobs_list)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)