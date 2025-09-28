from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Route chính
@app.route('/')
def index():
    return render_template('index.html')

# Route xử lý form liên hệ
@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    
    # Tạo đối tượng thông tin liên hệ
    contact_info = {
        'name': data.get('name'),
        'email': data.get('email'),
        'message': data.get('message'),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Ghi log vào file JSON
    try:
        with open('contact_log.json', 'a') as f:
            f.write(json.dumps(contact_info) + '\n')
    except Exception as e:
        print(f"Lỗi khi ghi file: {e}")
    
    # In ra console (cho mục đích debug)
    print(f"Thông tin liên hệ mới:")
    print(f"Tên: {contact_info['name']}")
    print(f"Email: {contact_info['email']}")
    print(f"Tin nhắn: {contact_info['message']}")
    print(f"Thời gian: {contact_info['timestamp']}")
    
    return jsonify({'success': True, 'message': 'Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm.'})

if __name__ == '__main__':
    app.run(debug=True)