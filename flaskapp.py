from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)     

@app.route("/")
def hello_jovian():
    jobs_list = load_jobs_from_db()
    return render_template('home.html' ,
                           jobs=jobs_list,
                           company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db)

@app.route('/always_ok', methods=['GET'])
def always_ok():
    return jsonify({'message': 'OK'}), 200

@app.route("api/prommetrics")
def metricsprom():
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)
