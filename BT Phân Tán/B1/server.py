import socket
def run_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1' # Localhost
    port = 65432
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server đang chạy tại {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Đã kết nối bởi: {addr}")
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Client gửi: {data}")
        response = f"Server đã nhận được: {data}"
        conn.send(response.encode('utf-8'))
        
    conn.close()
    print("Kết nối đã đóng.")

if __name__ == "__main__":
    run_server()