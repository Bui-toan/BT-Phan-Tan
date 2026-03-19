import numpy as np

# Tài nguyên hiện có trong hệ thống (R1, R2, R3)
available = np.array([3, 3, 2])

# Tài nguyên tối đa mỗi tiến trình cần
max_claim = np.array([
    [7, 5, 3], # P0
    [3, 2, 2], # P1
    [9, 0, 2]  # P2
])

# Tài nguyên đã cấp phát
allocation = np.array([
    [0, 1, 0], # P0
    [2, 0, 0], # P1
    [3, 0, 2]  # P2
])

# Tính toán Need = Max - Allocation
need = max_claim - allocation

def check_safe_state():
    work = np.copy(available)
    finish = [False] * len(max_claim)
    safe_sequence = []

    while len(safe_sequence) < len(max_claim):
        allocated_in_round = False
        for i in range(len(max_claim)):
            if not finish[i] and all(need[i] <= work):
                # Giả định tiến trình i mượn đủ, làm xong và trả lại hết
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(f"P{i}")
                allocated_in_round = True
                print(f"Cấp phát cho {safe_sequence[-1]}, tài nguyên mới: {work}")
        
        if not allocated_in_round: # Không tìm được tiến trình nào thỏa mãn
            return False, []
    return True, safe_sequence

is_safe, sequence = check_safe_state()
if is_safe:
    print(f"Hệ thống AN TOÀN. Thứ tự: {sequence}")
else:
    print("Hệ thống KHÔNG AN TOÀN (Nguy cơ Deadlock)!")