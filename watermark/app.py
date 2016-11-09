import os
from flask import Flask, request, redirect, url_for,render_template,jsonify
from werkzeug import secure_filename
import cv2

UPLOAD_FOLDER = '../static/uploads/'
DOWNLOAD_FOLDER = '../static/downloads/'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('upload.html')

@app.route('/add_mark', methods=['GET', 'POST'])
def add_mark():
    filepath =""
    if request.method == 'POST':
        img1 = request.files['img1']
        img2 = request.files['img2']
        if img1 and allowed_file(img1.filename) and img2 and allowed_file(img2.filename):
            file1name = secure_filename(img1.filename)
            img1.save(os.path.join(app.config['UPLOAD_FOLDER'], file1name))
            file2name = secure_filename(img2.filename)
            img2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2name))
            enc=encode(img1,img2)
            encname="enc.jpg"
            encpath=os.path.join(app.config['DOWNLOAD_FOLDER'], encname)
            cv2.imwrite(encpath,enc)
            dec=decode(enc)
            decname = "dec.jpg"
            decpath = os.path.join(app.config['DOWNLOAD_FOLDER'], decname)
            cv2.imwrite(decpath, dec)
    return jsonify(decpath='%s' %decpath,encpath='%s' %encpath)

def encode(imgfile1,imgfile2):
    img1=cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], imgfile1.filename))
    img2=cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'],imgfile2.filename))
    row,col,cannel=img1.shape
    img2=cv2.resize(img2,(col,row))
    res=(img1&252)+((img2&192)>>6)
    return res

def decode(enc):
    ori=(enc&3)*85
    return ori

if __name__=='__main__':
    app.run(threaded=True, port=5000,debug=True)