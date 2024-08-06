from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    info = data.get('info', '')

    # データをファイルに保存する
    with open('saved_data.txt', 'w', encoding='utf-8') as file:
        file.write(info)

    return jsonify({'message': '情報が保存されました'})

if __name__ == '__main__':
    app.run(debug=True)
