import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg_server = ('localhost', 8000)
print('Summoning a server at {} and port {}'.format(*msg_server))
s.bind(msg_server)

s.listen(1)

while True:
    print('Ready for action...')
    connection, client_addr = s.accept()
    try:
        print('Received a connection from: ', client_addr)
        while True:
            data = connection.recv(16)
            print('Something has arrived... {!r}'.format(data))
            if data:
                print('Reflecting data to client to signify message success.')
                connection.sendall(data)
                last_msg = time.time()
            else:
                print('dead air from: ', client_address)
                if time.time() - last_msg > 20:
                    print('shut it down')
                    s.close()
                    break
                break
            
    finally:
        connection.close()
