import time
import socket
from ping3 import ping

# Latency Calculation
def calculate_latency(host):
    try:
        rtt = ping(host, timeout=1)  # Send ping request
        if rtt is None:
            return "Error: Host unreachable or ping request timed out"
        return rtt * 1000  # Convert to milliseconds
    except Exception as e:
        return f"Error calculating latency: {str(e)}"

# Jitter Calculation (difference between successive latencies)
def calculate_jitter(host, num_pings=10):
    try:
        rtts = [ping(host, timeout=1) for _ in range(num_pings)]
        rtts = [rtt for rtt in rtts if rtt]  # Filter out None (failed pings)

        if len(rtts) < 2:
            return "Error: Not enough data for jitter calculation"
        
        jitter = sum(abs(rtts[i] - rtts[i-1]) for i in range(1, len(rtts))) / (len(rtts) - 1)
        return jitter * 1000  # Convert to milliseconds
    except Exception as e:
        return f"Error calculating jitter: {str(e)}"

# Bandwidth Calculation using a simulated file transfer
def calculate_bandwidth(host, port=443, chunk_size=32 * 1024, total_size=128 * 1024):  # 128KB test
    try:
        start_time = time.time()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Connection timeout
            s.connect((host, port))

            # Send data in chunks
            bytes_sent = 0
            while bytes_sent < total_size:
                try:
                    s.sendall(b'0' * min(chunk_size, total_size - bytes_sent))
                    bytes_sent += chunk_size
                except BrokenPipeError:
                    return "Error: Broken pipe - Connection closed prematurely"

        end_time = time.time()
        bandwidth = total_size / (end_time - start_time) / 1024 / 1024  # Bandwidth in MBps
        return bandwidth
    except socket.gaierror:
        return "Error: Invalid host or host not found"
    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"Error during bandwidth test: {e}"
