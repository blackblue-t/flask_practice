from flask import Flask
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def helloFlask():
    return 'Hello Flask!'

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')
    #這會在預設的 Web 瀏覽器中開啟應用程式的 URL (http://127.0.0.1:5000/)。

if __name__ == '__main__':
    # 啟動 Flask 前啟動瀏覽器
    Timer(1, open_browser).start()
    #用於延遲執行 open_browser，確保瀏覽器在伺服器啟動後打開。
    app.run(host='0.0.0.0', port=5000)
    