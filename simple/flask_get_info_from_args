from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_get', methods=['GET'])
def hello_get():
    username = request.args.get('username')
    userage = request.args.get('userage')
    outStr = """
    <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
    """

    if username == None:
        outStr += """
        Who are you?
        """
    else:
        outStr += """
        Hello %s !
        """%(username)
        if userage != None:
            outStr += """
            You are %s years old.
            """%(userage)

    outStr += """
        </body>
    </html>
    """
    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)