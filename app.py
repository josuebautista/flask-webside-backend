from flask import Flask, jsonify, render_template
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def home_route():
    jobs_list = load_jobs_from_db()
    return render_template(
        'home.html', 
        jobs=jobs_list, 
        company_name='My company name'
        )

@app.route("/home", methods=['GET', 'POST'])
def home():
    return home_route()

@app.route('/jobs')
def list_jobs():
    return jsonify(
        load_jobs_from_db()
        )

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)