# PALESTINE-Free Tool

**PALESTINE-Free** is a simple DoS tool using TCP Flood and HTTP requests.

---

## Purpose of the Tool

To perform a Denial of Service (DoS) attack on a server or a website running on the HTTP protocol (non-encrypted).

The goal is to flood the server with a large number of connections and requests, consuming its resources (CPU, RAM, and network connections).

As a result, the server becomes slow or stops responding.

---

## How It Works

After entering the input data, the tool starts opening multiple threads as specified.

Each thread opens a TCP connection to the target server.

It sends random HTTP GET requests with various headers like `User-Agent` and `Referer` to simulate real requests.

It also sends random data (bytes) after the requests to increase pressure.
