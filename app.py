from flask import Flask, jsonify, render_template, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
import re

app = Flask(__name__)

@app.route("/")
def home_route():
    jobs_list = load_jobs_from_db()
    return render_template(
        'home.html', 
        jobs=jobs_list, 
        company_name='My company name',
        title='Home'
        )

@app.route("/home", methods=['GET', 'POST'])
def home():
    return home_route()

@app.route('/jobs')
def list_jobs():
    return jsonify(
        load_jobs_from_db()
        )

@app.route('/job/<id>')
def show_job(id: int):
    job = load_job_from_db(id)
    if not job:
        return 'Not Found', 404
    return render_template(
        'job_page.html', 
        job=job, 
        title=job['title'],
        company_name='My company name'
        )

@app.route('/api/job/<id>')
def show_job_json(id: int):
    job = load_job_from_db(id)
    return jsonify(job)


@app.route('/job/<id>/apply', methods=['POST'])
def apply_job(id: int):
    job = load_job_from_db(id)
    data = request.form
    add_application_to_db(id, data)
    return render_template(
        'application_submited.html', 
        company_name='My company name',
        application = data, 
        title= 'Submited',
        role=job
        )

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)