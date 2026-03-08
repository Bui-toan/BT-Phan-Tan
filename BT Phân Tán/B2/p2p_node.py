import socket
import threading

def listen_for_messages(my_port):
    """Luồng này đóng vai trò Server: Chờ nhận tin nhắn"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', my_port))
    server.listen(5)
    print(f"[ĐANG CHẠY] Peer đang lắng nghe tại Port: {my_port}")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode('utf-8')
        print(f"\n[TIN NHẮN MỚI từ {addr}]: {data}")
        print("Nhập Port người nhận (hoặc 'exit' để thoát): ", end="")
        conn.close()

def send_messages():
    """Luồng này đóng vai trò Client: Gửi tin nhắn đi"""
    while True:
        target_port = input("Nhập Port người nhận (hoặc 'exit' để thoát): ")
        if target_port.lower() == 'exit':
            break
        
        message = input("Nội dung tin nhắn: ")
        
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', int(target_port)))
            client.send(message.encode('utf-8'))
            client.close()
            print("[HỆ THỐNG] Đã gửi thành công!")
        except Exception as e:
            print(f"[LỖI] Không thể kết nối tới Peer tại Port {target_port}: {e}")

if __name__ == "__main__":
    my_port = int(input("Nhập Port cho Peer này (VD: 5001, 5002...): "))
    
    # Chạy luồng lắng nghe (Server) ngầm
    listener = threading.Thread(target=listen_for_messages, args=(my_port,), daemon=True)
    listener.start()
    
    # Chạy luồng gửi tin (Client) ở luồng chính
    send_messages()