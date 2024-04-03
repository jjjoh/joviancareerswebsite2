from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from prometheus_flask_exporter import PrometheusMetrics
import datetime


app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Métriques par défaut pour les requêtes HTTP
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route("/")
def hello_jovian():
    jobs_list = load_jobs_from_db()
    return render_template('home.html' ,
                           jobs=jobs_list,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

@app.route('/always_ok', methods=['GET'])
def always_ok():
    return jsonify({'message': 'OK'}), 200

@app.route("/time")
def time():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)
