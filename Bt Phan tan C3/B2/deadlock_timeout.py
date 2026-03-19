import threading
import time

# Khởi tạo 2 tài nguyên đóng vai trò là các khóa (Lock)
resource1 = threading.Lock()
resource2 = threading.Lock()

def process_a():
    print("A: Đang lấy Resource 1...")
    with resource1:
        print("A: Đã giữ R1. Ngủ 1s để B kịp lấy R2 (tạo deadlock)...")
        time.sleep(1) 
        
        print("A: Đang cố lấy Resource 2 (có timeout 3s)...")
        # acquire(timeout=3) nghĩa là: Chờ 3 giây, nếu không được thì bỏ qua
        success = resource2.acquire(timeout=3)
        
        if success:
            print("A: Tuyệt vời! Đã giữ cả R1 và R2.")
            resource2.release()
        else:
            print("A: Quá lâu rồi! Giải phóng R1 để tránh Deadlock.")
    # Khi thoát khỏi khối 'with', resource1 tự động được release

def process_b():
    print("B: Đang lấy Resource 2...")
    with resource2:
        print("B: Đã giữ R2. Ngủ 1s để A kịp lấy R1...")
        time.sleep(1)
        
        print("B: Đang cố lấy Resource 1 (có timeout 3s)...")
        success = resource1.acquire(timeout=3)
        
        if success:
            print("B: Tuyệt vời! Đã giữ cả R2 và R1.")
            resource1.release()
        else:
            print("B: Timeout rồi! Giải phóng R2 để nhường đường.")

# Chạy thử
thread1 = threading.Thread(target=process_a)
thread2 = threading.Thread(target=process_b)
thread1.start()
thread2.start()

