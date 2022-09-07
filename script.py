"""
/var/log/customlog.log
export to /var/exporter/metrics
expose this on 0.0.0.0:9800/metrics
Rest API

"""

if __name__ == "__main__":
    f_log = open("/var/log/customlog.log","r")
    f_metric = open("/var/exporter/metrics","w")
    f_content = f_log.read()
    if '400' in f_content:
        f_metric.write("FourHundredErrors: 1")
    f_log.close()
    f_metric.close()
