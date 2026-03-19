import multiprocessing
import time
import random

def worker(conn, worker_id):
    # Giả lập tính toán
    process_time = random.uniform(1, 3)
    time.sleep(process_time)
    
    result = f"Dữ liệu từ Worker {worker_id} (xử lý trong {process_time:.2f}s)"
    
    # Gửi kết quả về cho cha
    conn.send(result)
    conn.close()

if __name__ == "__main__":
    num_workers = 4
    processes = []
    receivers = []

    print(f"--- Cha bắt đầu tạo {num_workers} tiến trình con ---")

    for i in range(num_workers):
        # Tạo Pipe riêng cho từng Worker
        p_conn, c_conn = multiprocessing.Pipe()
        
        p = multiprocessing.Process(target=worker, args=(c_conn, i + 1))
        processes.append(p)
        receivers.append(p_conn) # Cha giữ đầu nhận
        p.start()

    # d) Cha đọc và xử lý từng dữ liệu nhận được
    print("[Cha] Đang ngồi đợi dữ liệu từ các con...\n")
    for idx, conn in enumerate(receivers):
        # recv() sẽ đợi cho đến khi Worker i gửi dữ liệu
        data = conn.recv()
        print(f"[Cha] Thu thập: {data}")

    for p in processes:
        p.join()

    print("\n[Cha] Tất cả các con đã báo cáo xong.")