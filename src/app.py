from flask import Flask, request, jsonify, render_template
import datetime

import utils

launch_at = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)


@app.route("/json")
def send_json():
    global launch_at
    return jsonify({'launch_at': launch_at,
                    'Hostname': utils.get_hostname(),
                    'LocalAddress': utils.get_local_address(),
                    'RemoteAddress':  request.remote_addr,
                    'visitor_addrs': utils.record_visitors(request.remote_addr).items(),
                    'Server Hit': str(utils.hit_count())})


@app.route("/")
def index():
    global launch_at
    return render_template('index.html',
                           launch_at=launch_at,
                           Hostname=utils.get_hostname(),
                           localaddress=utils.get_local_address(),
                           remote_addr=request.remote_addr,
                           visitor_addrs=utils.record_visitors(request.remote_addr).items(),
                           hits=str(utils.hit_count()))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
