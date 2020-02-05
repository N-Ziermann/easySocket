import socket

# Setting up the connection:


def host_tcp(my_ip="0.0.0.0", port=12345):     # hosts a TCP connection and waits for client
    s = socket.socket()
    s.bind((my_ip, port))
    s.listen(5)
    c, address = s.accept()
    return c


def connect_tcp(ip, port=12345):   # connects to TCP from ip under given port
    s = socket.socket()
    s.connect((ip, port))
    return s

# Ways of sending data without needing to think about data limits:


def send_file(location, recipient):       # makes it possible to send images
    if isinstance(recipient, socket.socket):
        file = open(location, "rb").read()
        send_repeat(file, recipient)
    else:
        raise Exception("Recipient needs to be of the type: socket.socket")
        quit()


def send_text(text, recipient):           # makes it possible to send texts bigger than the max byte size for .send
    if isinstance(recipient, socket.socket):
        byte_text = text.encode()
        send_repeat(byte_text, recipient)
    else:
        raise Exception("Recipient needs to be of the type: socket.socket")
        quit()


def send_repeat(data, r):            # sends data in for loop so that send limit (1406 bytes) isn't exceeded
    split = [data[i:i + 1024] for i in range(0, len(data), 1024)]
    length = len(split)
    r.send(str(length).encode())    # sends over the amount of packages the recipient needs to listen for
    r.recv(1024)                    # makes sure the package arrived
    for i in range(0, length):      # sends over the text in 1024 byte steps
        r.send(split[i])
    r.recv(1024)


# Receiving end of send functions above:


def rcv_data(sender):   # returns data send from other site in byte format(independent of length)
    if isinstance(sender, socket.socket):
        data_len = int(sender.recv(1024).decode())
        sender.send("Received".encode())
        data = sender.recv(1024)                 # receive the image
        for i in range(0, data_len-1):
            data += sender.recv(1024)
        sender.send("Received".encode())        # tells the sender that everything arrived
        return data
    else:
        raise Exception("Sender needs to be of the type: socket.socket")
        quit()


# Written by N-Ziermann
