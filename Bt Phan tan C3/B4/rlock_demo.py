import threading

# Thử thay threading.RLock() bằng threading.Lock() bạn sẽ thấy chương trình bị treo (Deadlock)
reentrant_lock = threading.RLock()

def function_A():
    with reentrant_lock:
        print("Đang ở trong Function A")
        function_B() # Gọi hàm B, hàm B lại yêu cầu cùng một khóa
    print("Thoát khỏi Function A")

def function_B():
    with reentrant_lock:
        print("Đang ở trong Function B - Vẫn an toàn nhờ RLock!")
    print("Thoát khỏi Function B")

if __name__ == "__main__":
    print("--- THỬ NGHIỆM RLOCK ---")
    t = threading.Thread(target=function_A)
    t.start()
    t.join()
    print("Hoàn thành!")