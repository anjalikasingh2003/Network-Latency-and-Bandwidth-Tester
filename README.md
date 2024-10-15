# Network Latency, Jitter, and Bandwidth Tester

This project is a web-based tool for testing network performance by measuring latency, jitter, and bandwidth between a client and a specified host. The backend is powered by Flask and Python, while the frontend is built using HTML, CSS, and JavaScript. The tool performs ICMP-based ping tests for latency and jitter, and TCP socket-based tests for bandwidth.

## Features
- **Latency Measurement**: Calculates the round-trip time (RTT) using ICMP (ping).
- **Jitter Measurement**: Calculates the variation in latency over multiple ping requests.
- **Bandwidth Measurement**: Measures bandwidth by sending data over a TCP connection.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (AJAX)
- **Network Performance Measurement**:
  - Python (`ping3` library for ping requests, `socket` for TCP connections)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Step-by-Step Guide
1. Clone the repository or download the zip file of the project and extract it.
2. Navigate to the project directory:
    ```bash
    cd NetworkTester
    ```
3. Install the required dependencies:
    ```bash
    pip install flask ping3
    ```
4. Start the Flask server:
    ```bash
    python app.py
    ```
5. Open a web browser and go to `http://127.0.0.1:5000/`.
6. Enter a hostname (e.g., `google.com`) in the input field and click "Test Network."

## Functionality

### Latency Calculation
The tool sends ICMP echo requests (pings) to the target host and measures the round-trip time (RTT).

### Jitter Calculation
The tool measures jitter by calculating the variation in RTT over multiple pings.

### Bandwidth Calculation
The bandwidth is calculated by sending a known amount of data over a TCP connection and measuring the time it takes to complete the transfer.


