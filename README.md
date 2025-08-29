**EchoServer** 

EchoServer is a minimal Python TCP server that listens for incoming connections, receives messages, and echoes them back to the client. It’s useful for learning socket programming, testing client-server communication, or building simple networking demos.

### Features

* **TCP Echo Server**: Receives and returns data to connected clients.
* **Connection Logging**: Prints connection events and received data.
* **Timeout Handling**: Closes idle connections after 20 seconds of inactivity.
* **Simple Setup**: Easy to run on `localhost` with no external dependencies.

### Technologies Used

* **Python 3**: The language used to build the script.
* **socket**: For handling TCP/IP communication.
* **time**: For connection timeout tracking.

### Usage

1. **Clone the Repository**

```bash
git clone https://github.com/zared1/EchoServer.git
cd EchoServer
```

2. **Run the Server**

```bash
python server-for-receiving-messages.py
```

The server will start on `localhost:8000` and wait for incoming connections.

### How It Works

1. The server binds to `localhost` on port `8000`.
2. When a client connects, it listens for incoming messages in 16-byte chunks.
3. Any received message is echoed back to the client.
4. If no data is received for 20 seconds, the server shuts down the connection.

### Example

Use a simple TCP client (like `telnet`, `nc`, or a custom Python script) to send a message:

```bash
nc localhost 8000
```

Type a message and press Enter — the server will send it back.

Happy coding!
