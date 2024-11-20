from flask import Flask, request
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'GET':
        return outStr%('')
    elif request.method == 'POST':
        username = request.form.get('username')
        return outStr%('Hello %s'%(username))
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/hello_post')
    #這會在預設的 Web 瀏覽器中開啟應用程式的 URL

if __name__ == '__main__':
    Timer(0.5, open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=5000)