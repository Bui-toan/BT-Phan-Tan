import multiprocessing
import concurrent.futures
import time
import math

# Hàm kiểm tra số nguyên tố (Tác vụ nặng CPU)
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

# Hàm tính tổng các số nguyên tố trong một danh sách
def sum_primes_in_chunk(numbers):
    return sum(n for n in numbers if is_prime(n))

if __name__ == "__main__":
    # d) Bộ dữ liệu lớn (1 triệu số)
    limit = 1_000_000
    numbers = list(range(limit))
    
    # b) Cho người dùng chọn số tiến trình
    num_processes = int(input("Nhập số tiến trình chạy song song (vd: 4 hoặc 8): "))

    # Chia nhỏ dữ liệu (câu a)
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    print(f"\n--- Đang tính tổng số nguyên tố từ 0 đến {limit} ---")

    # 1. Chạy Đơn tiến trình (Single Process)
    start = time.time()
    result_seq = sum_primes_in_chunk(numbers)
    time_seq = time.time() - start
    print(f"[1] Đơn tiến trình: {time_seq:.4f} giây")

    # 2. Chạy Process Pool (Câu a, c)
    start = time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(sum_primes_in_chunk, chunks)
        result_process = sum(results)
    time_process = time.time() - start
    print(f"[2] Process Pool ({num_processes} procs): {time_process:.4f} giây")

    # 3. Chạy Thread Pool (Câu e)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(sum_primes_in_chunk, chunks))
        result_thread = sum(results)
    time_thread = time.time() - start
    print(f"[3] Thread Pool ({num_processes} threads): {time_thread:.4f} giây")

    print("\n--- KẾT QUẢ SO SÁNH ---")
    print(f"Process Pool nhanh gấp {time_seq/time_process:.2f} lần so với chạy thường.")
    print(f"Process Pool nhanh gấp {time_thread/time_process:.2f} lần so với Thread Pool.")