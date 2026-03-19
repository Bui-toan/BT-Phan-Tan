import threading
import time

# Tạo Semaphore cho phép tối đa 3 tiến trình dùng chung tài nguyên
semaphore = threading.Semaphore(3)

def access_resource(id):
    print(f"Tiến trình {id}: Đang xếp hàng...")
    with semaphore:
        print(f"Tiến trình {id}: Đã vào hệ thống, đang xử lý...")
        time.sleep(2)
        print(f"Tiến trình {id}: Đã hoàn thành và rời đi.")

# Tạo 6 tiến trình cùng tranh giành 3 vị trí
threads = []
for i in range(6):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()