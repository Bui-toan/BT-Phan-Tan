from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    # Giả lập đơn hàng
    order = {"order_id": order_id, "user_id": "1", "amount": 100}
    
    # Gọi sang User Service bằng tên service trong docker-compose
    try:
        response = requests.get(f"http://user-service:5001/users/{order['user_id']}")
        user_info = response.json()
    except Exception as e:
        user_info = "Could not fetch user info"

    return jsonify({
        "order_details": order,
        "customer_info": user_info
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)