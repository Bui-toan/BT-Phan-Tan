import socket
import pickle
import struct

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def recv_all(sock, n):
    # Hàm bổ trợ để nhận đủ n bytes dữ liệu
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet: return None
        data.extend(packet)
    return data

def handle_worker():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 9999))
        
        # 1. Nhận 4 byte đầu tiên để biết độ dài
        raw_msglen = recv_all(client, 4)
        if not raw_msglen: return
        msglen = struct.unpack(">I", raw_msglen)[0]
        
        # 2. Nhận toàn bộ dữ liệu dựa trên độ dài đã biết
        print(f"Đang tải dữ liệu ({msglen} bytes)...")
        data = recv_all(client, msglen)
        numbers = pickle.loads(data)
        
        # 3. Tính toán
        print(f"Đang xử lý {len(numbers)} số...")
        result = sum(n for n in numbers if is_prime(n))
        
        # 4. Gửi kết quả về
        client.send(pickle.dumps(result))
    finally:
        client.close()
        print("Đã hoàn thành và đóng kết nối.")

if __name__ == "__main__":
    handle_worker()