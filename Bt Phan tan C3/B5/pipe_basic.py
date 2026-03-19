import multiprocessing
import time

def child_task(conn):
    # a) Nhận dữ liệu từ cha
    msg_from_parent = conn.recv()
    print(f"[Con] Đã nhận từ Cha: {msg_from_parent}")
    
    # b) & c) Gửi dữ liệu phản hồi về cho cha
    time.sleep(1)
    print("[Con] Đang gửi phản hồi...")
    conn.send("Con đã nhận được tin và hoàn thành nhiệm vụ!")
    
    conn.close()

if __name__ == "__main__":
    # Khởi tạo Pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Tạo tiến trình con
    p = multiprocessing.Process(target=child_task, args=(child_conn,))
    p.start()

    # a) Cha gửi dữ liệu
    print("[Cha] Gửi yêu cầu cho con...")
    parent_conn.send("Hãy quét nhà giúp cha.")

    # c) Cha nhận dữ liệu từ con (Giao tiếp 2 chiều)
    response = parent_conn.recv()
    print(f"[Cha] Phản hồi từ con: {response}")

    p.join()
    print("Kết thúc phiên giao tiếp.")