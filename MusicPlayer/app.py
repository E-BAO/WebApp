from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html',message=0,dirname='',murl=0,imgurl='images/pc.jpg')

@app.route('/<Artist>', methods=['GET','POST'])
def Artist_form(Artist):
    dir_list = [x for x in os.listdir('static/%s/mp3.' %Artist) if os.path.splitext(x)[1]=='.mp3']
    imgurl='%s/image/014.png'%Artist
    return render_template('index.html',message='%s list' %Artist, dir_list=dir_list,dirname='%s'%Artist,imgurl=imgurl,title="title of the music",murl=0)

@app.route('/<Artist>/<SongNum>', methods=['GET','POST'])
def Song_form(Artist,SongNum):
    dir_list = [x for x in os.listdir('static/%s/mp3.' %Artist) if os.path.splitext(x)[1]=='.mp3']
    title=SongNum[0:3]
    murl='%s/mp3/%s.mp3' %(Artist,title)
    imgurl='%s/image/%s.png'%(Artist,title)
    turl='static/%s/text/%s.txt' %(Artist,title)
    f = open(turl,'r') 
    lines = f.readlines() 
    return render_template('index.html',message='%s list' %Artist, dir_list=dir_list,dirname='%s'%Artist,title=title,murl=murl,imgurl=imgurl,lines=lines)

if __name__ == '__main__':
    app.run()
