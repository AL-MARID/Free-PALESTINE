<p align="center">
  <img src="Free-PALESTINE.jpg" alt="Free-PALESTINE" width="400" />
</p>

# Detailed Explanation of the Tool (`Free-PALESTINE Tool`)

## Main Objective

This tool is designed to perform a **Denial of Service (`DoS`)** attack against web servers using `HTTP`/`HTTPS` requests.  
The main goals of the tool are:

- Flood the target server with a massive number of requests.  
- Consume server resources (`CPU`, `memory`, and `network connections`).  
- Make the server slow or completely unresponsive.

---

## How Does the Tool Work?

### 1. Data Input:

The user is asked to enter:

- The target `IP address`.  
- The `port` (e.g., `80` for `HTTP` or `443` for `HTTPS`).  
- The number of packets sent per second.  
- The number of `threads`.

---

### 2. Starting the Attack:

- The tool creates several `threads` (based on the specified number).  
- Each thread executes the attack in parallel.

---

### 3. Attack Mechanism for Each Thread:

**Establishing a `TCP` Connection:**

- Connects to the target server via the specified `port`.  
- If the port is `443` (`HTTPS`), it uses an encrypted connection (`SSL/TLS`).

**Creating Fake `HTTP` Requests:**

- The `HTTP` method is chosen randomly (`GET`, `POST`, `PUT`, `DELETE`, ...).  
- Fake paths are generated such as `/api/user` or `/search?q=...`.  
- Random headers are added, including:

  - `User-Agent`: Pretending to be different browsers (`Chrome`, `Firefox`, `iPhone`, ...).  
  - `Referer`: Fake search links (`Google`, `Bing`, ...).  
  - `Cookies`: Random identification data.  
  - `X-Forwarded-For`: Spoofed `IP` addresses.

**Sending Extra Data:**

- After the main request, random data (up to `8192` bytes) is sent to increase pressure.  
- The data may be compressed using `gzip` to add more load to the server.

**Retry on Failure:**

- If the connection fails, the thread retries after a short wait.

---

## Advanced Features

### Request Variety:

- Weighted use of `GET` / `POST` / `PUT` / `DELETE` requests.  
- Random `POST` data (`JSON`, `XML`, `Form Data`).  
- `gzip`-compressed content to increase server load.

### Attack Statistics:

Real-time display of:

- Packets sent per second (`PPS`).  
- Bandwidth usage (`Mbps`).  
- Number of successful/failed connections.  
- Attack duration.


## Download:
```bash
git clone https://github.com/AL-MARID/Free-PALESTINE.git
```
## Enter the tool directory:
```bash
cd Free-PALESTINE
```
## Install the required Python library:
```bash
pip3 install -r requirements.txt
```
## Run the tool.
```bash
python3 Free-PALESTINE.py
```





<p align="center">
  <img src="Free-PALESTINE.jpg" alt="Free-PALESTINE" width="400" />
</p>


## "Palestine is the land of pride and dignity, and its people are a symbol of resilience and determination. Despite all the challenges and sacrifices, the Palestinian remains steadfast in their right and their land. It is not just a national cause, but a story of humanity and honor that lives in the hearts of millions. We stand with Palestine with love and unwavering support, believing that freedom is inevitably coming.

This digital tribute represents more than just a flag – it is a symbol of resistance and hope. Your sacrifices are never forgotten, O Palestine."
# Free-PALESTINE
