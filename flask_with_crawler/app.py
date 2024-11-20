from flask import Flask,request
import simple_crawler as s
app = Flask(__name__)

@app.route('/pttcrawler',methods=['GET','POST'])
def pttcrawler():
    askStr = """
    <html>
    <form action="/pttcrawler" method="POST">
        <label>What terms do you want to crawl on ptt?</label>
        <br>
        <input type="textbox" name="terms">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'GET':
        return askStr%('')
    elif request.method == 'POST':
        terms = request.form.get('terms')
        title = s.simple_scraper(terms)
        return askStr%(f'''這是最新的一條標題
                       <br>
                       {title}''')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)