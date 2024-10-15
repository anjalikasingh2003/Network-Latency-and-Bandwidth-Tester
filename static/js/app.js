document.getElementById('network-form').addEventListener('submit', function (event) {
    event.preventDefault();

    let host = document.getElementById('host').value;
    let port = document.getElementById('port').value;

    fetch('/test_network', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ host: host, port: port })
    })
    .then(response => response.json().then(data => ({
        status: response.status,
        body: data
    })))
    .then(({status, body}) => {
        document.getElementById('results').style.display = 'block';

        // Check if we received an error
        if (status !== 200) {
            document.getElementById('latency').textContent = body.latency || 'Error';
            document.getElementById('jitter').textContent = body.jitter || 'Error';
            document.getElementById('bandwidth').textContent = body.bandwidth || 'Error';
        } else {
            document.getElementById('latency').textContent = `${body.latency.toFixed(2)} ms`;
            document.getElementById('jitter').textContent = `${body.jitter.toFixed(2)} ms`;
            document.getElementById('bandwidth').textContent = `${body.bandwidth.toFixed(2)} MBps`;
        }
    })
    .catch(error => {
        document.getElementById('results').style.display = 'block';
        document.getElementById('latency').textContent = 'Error occurred';
        document.getElementById('jitter').textContent = 'N/A';
        document.getElementById('bandwidth').textContent = 'N/A';
    });
});
