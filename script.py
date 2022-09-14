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
def readLog():
    f_log = open("/var/log/customlog.log","r")
    f_content = f_log.read()
    count_message = "FourHundredErrors: "+str(f_content.count("HTTP/1.1\" 401"))
    f_log.close()
    return count_message

if __name__ == "__main__":
    @app.route("/metrics", methods=["GET"])
    def getMetrics():
        return readLog()
    app.run(port=8099)
