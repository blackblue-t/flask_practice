from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/hello_cat')
def hello_cat():
    outStr = """
    <link href="/static/css/mystyle.css" rel="stylesheet" type="text/css">
    <div>
        CATS are awesome.
    </div>
    <div class="test">
        CATS are awesome.
    </div>
    <div>
        <img src="/static/image/cat.jpg" width="400">
    </div>
    """

    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
