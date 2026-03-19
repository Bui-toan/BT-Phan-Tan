import socket
import pickle
import struct

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))
    server.listen(2)
    
    print("Server đang đợi các máy con (Workers) kết nối...")
    
    # Chia nhỏ dữ liệu (Mỗi bên 500k số)
    data_to_solve = [list(range(0, 500000)), list(range(500000, 1000000))]
    results = []

    for i in range(2):
        conn, addr = server.accept()
        print(f"Máy con {addr} đã kết nối.")
        
        # 1. Chuẩn bị dữ liệu
        payload = pickle.dumps(data_to_solve[i])
        # 2. Gửi độ dài dữ liệu trước (4 bytes)
        conn.sendall(struct.pack(">I", len(payload)) + payload)
        
        # 3. Nhận lại kết quả
        res_data = conn.recv(1024)
        if res_data:
            results.append(pickle.loads(res_data))
        conn.close()

    print(f"--- KẾT QUẢ CUỐI CÙNG ---")
    print(f"Tổng các số nguyên tố tìm được: {sum(results)}")

if __name__ == "__main__":
    run_server()