from flask import *
from trans import sualoi

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
async def check_tweet():
    if request.method=='POST':
        tweet=request.form['tweet']
        print(sualoi(tweet))
        return render_template('index.html',data=str(sualoi(tweet)),tweet=tweet)
    
    if request.method=='GET':
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)