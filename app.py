from flask import Flask,request,jsonify,render_template
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://test:sparta@cluster00.aw629as.mongodb.net/?retryWrites=true&w=majority')
db = client.giid

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/fans",methods=['POST'])
def post_fans():
    x = datetime.datetime.now()
    year =x.strftime("%G")
    comment_receive = request.form['comment_give']
    username_receive = request.form['username_give']
    doc = {
        'username': username_receive,
        'comments': comment_receive,
        'year': year
    }
    db.webfans.insert_one(doc)
    return jsonify({'msg': 'Oke thanks'})

@app.route('/fans',methods=['GET'])
def get_fans():
    comments = list(db.webfans.find({},{'_id':False}))
    return jsonify({
        'msg': 'Okay',
        'fan_komen': comments
    })

if __name__=='__main__':
    app.run('0.0.0.0',5000,debug=True)