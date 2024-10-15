from flask import Flask, render_template, request, jsonify
from network_tester import calculate_latency, calculate_jitter, calculate_bandwidth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_network', methods=['POST'])
def test_network():
    data = request.get_json()
    host = data.get('host')
    port = data.get('port', 443)  # Default to port 443 if not provided

    if not host:
        return jsonify({'error': 'Host cannot be empty'}), 400
    if not port or not str(port).isdigit() or int(port) <= 0 or int(port) > 65535:
        return jsonify({'error': 'Invalid port number'}), 400

    # Run the network tests
    latency = calculate_latency(host)
    jitter = calculate_jitter(host)
    bandwidth = calculate_bandwidth(host, int(port))

    # If any of the results is an error message, return it as an error
    if isinstance(latency, str) or isinstance(jitter, str) or isinstance(bandwidth, str):
        return jsonify({
            'latency': latency,
            'jitter': jitter,
            'bandwidth': bandwidth
        }), 400  # HTTP 400 Bad Request for error

    return jsonify({
        'latency': latency,
        'jitter': jitter,
        'bandwidth': bandwidth
    })

if __name__ == '__main__':
    app.run(debug=True)
