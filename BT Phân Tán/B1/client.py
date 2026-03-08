import socket

def run_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 65432
    client_socket.connect((host, port))

    message = "Chào Server! Mình là Client đây."
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(f"Phản hồi từ Server: {data}")

    client_socket.close()

if __name__ == "__main__":
    run_client()