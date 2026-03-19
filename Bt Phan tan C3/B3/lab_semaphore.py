import threading
import time
import random

# --- Câu a: Mô phỏng phòng học giới hạn k=3 người ---
def access_room(user_id, semaphore):
    print(f"User {user_id}: Đang đợi bên ngoài phòng...")
    
    # acquire() sẽ giảm counter của semaphore. Nếu = 0, luồng sẽ đợi ở đây.
    with semaphore:
        print(f"==> User {user_id}: ĐÃ VÀO PHÒNG (Đang có {3 - semaphore._value} người bên trong)")
        
        # Mô phỏng thời gian làm việc trong phòng
        work_time = random.uniform(1, 3)
        time.sleep(work_time)
        
        print(f"<-- User {user_id}: Rời phòng sau {work_time:.2f}s.")
    # Khi thoát block 'with', semaphore.release() tự động được gọi

# --- Câu b: Ghi file đồng bộ (Sử dụng Binary Semaphore k=1) ---
def write_to_file(thread_id, binary_semaphore, filename):
    with binary_semaphore:
        print(f"Thread {thread_id}: Đang ghi vào file...")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Dòng được ghi bởi Thread-{thread_id} lúc {time.ctime()}\n")
            time.sleep(1) # Mô phỏng việc ghi file tốn thời gian
        print(f"Thread {thread_id}: Ghi xong.")

def run_lab():
    print("--- BẮT ĐẦU CÂU (A): GIỚI HẠN TRUY CẬP ---")
    # Khởi tạo Semaphore với k=3 (Câu a)
    room_limit = threading.Semaphore(3)
    threads_a = []
    
    for i in range(1, 11): # n=10 người dùng
        t = threading.Thread(target=access_room, args=(i, room_limit))
        threads_a.append(t)
        t.start()
    
    for t in threads_a:
        t.join()

    print("\n--- BẮT ĐẦU CÂU (B): GHI FILE ĐỒNG BỘ ---")
    # Khởi tạo Semaphore với k=1 để hoạt động như một cái Lock (Câu b)
    file_mutex = threading.Semaphore(1)
    filename = "log_output.txt"
    
    # Xóa nội dung file cũ nếu có
    open(filename, "w").close()

    threads_b = []
    for i in range(5):
        t = threading.Thread(target=write_to_file, args=(i, file_mutex, filename))
        threads_b.append(t)
        t.start()

    for t in threads_b:
        t.join()
    print(f"\nKiểm tra file '{filename}' trong thư mục để xem kết quả.")

if __name__ == "__main__":
    run_lab()