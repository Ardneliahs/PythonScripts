"""
/var/log/customlog.log 400 errors
export to /var/exporter/metrics
expose this on 0.0.0.0:9800/metrics
Rest API

@app.route is a decorator that turns a regular Python function
into a Flask view function, which converts the function’s return
value into an HTTP response to be displayed by an HTTP client,
such as a web browser.

"""
from flask import Flask
app = Flask(__name__)
if __name__ == "__main__":
    f_log = open("/var/log/customlog.log","r")
#    f_metric = open("/var/exporter/metrics","w")
    f_content = f_log.read()
    count_message = "FourHundredErrors: "+str(f_content.count("400"))
#    f_metric.write(count_message)
    f_log.close()
#    f_metric.close()
    @app.route("/metrics", methods=["GET"])
    def getMetrics():
        return count_message

    app.run(port=8099)
