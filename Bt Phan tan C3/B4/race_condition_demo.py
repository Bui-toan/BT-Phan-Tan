import threading
import time

# Biến dùng chung
counter = 0
# Khởi tạo Lock
lock = threading.Lock()

def increase_without_lock(iterations):
    global counter
    for _ in range(iterations):
        # Race condition xảy ra ở đây
        current = counter
        counter = current + 1

def increase_with_lock(iterations):
    global counter
    for _ in range(iterations):
        # Chỉ một luồng được phép vào "vùng tới hạn" (critical section)
        with lock:
            counter += 1

def run_test(use_lock=False):
    global counter
    counter = 0
    threads = []
    iterations = 100000
    num_threads = 10
    
    start_time = time.time()
    for i in range(num_threads):
        target_func = increase_with_lock if use_lock else increase_without_lock
        t = threading.Thread(target=target_func, args=(iterations,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        
    end_time = time.time()
    
    status = "CÓ LOCK" if use_lock else "KHÔNG LOCK"
    print(f"[{status}]")
    print(f"- Giá trị counter cuối cùng: {counter:,}")
    print(f"- Giá trị kỳ vọng:           {num_threads * iterations:,}")
    print(f"- Thời gian thực thi:        {end_time - start_time:.4f}s\n")

if __name__ == "__main__":
    print("--- BẮT ĐẦU THỬ NGHIỆM RACE CONDITION ---\n")
    # Chạy không có lock để thấy lỗi
    run_test(use_lock=False)
    # Chạy có lock để thấy sự chính xác
    run_test(use_lock=True)