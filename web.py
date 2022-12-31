from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)




@app.route('/')
@app.route('/home')
def Home_Page():
    return render_template('home.html')

@app.route('/about_sheikh')
def About_Sheikh_Page():
    return render_template('about_sheikh.html')

@app.route('/about_us')
def About_Us_Page():
    return render_template('about_us.html')

@app.route('/contact')
def Contact_Page():
    return render_template('contact.html')

@app.route('/gallery')
def Gallery_Page():
    return render_template('gallery.html')

@app.route('/publish')
def Our_Publish_Page():
    return render_template('publish.html')

@app.route('/sahihu_muslim')
def Sahihu_Muslim_Page():
    return render_template('sahihu_muslim.html')

@app.route('/sahihul_bukhari')
def Sahihul_Bukhari_Page():
    return render_template('sahihul_bukhari.html')

@app.route('/abu_dawoud')
def Abu_Dawoud_Page():
    return render_template('abu_dawoud.html')

@app.route('/fatwas')
def Fatwas_Page():
    return render_template('fatwas.html')

@app.route('/videos')
def Videos_Page():
    return render_template('videos.html')

@app.route('/sermons')
def Sermons_Page():
    return render_template('sermons.html')

@app.route('/lectures')
def Lectures_Page():
    return render_template('lectures.html')

@app.route('/sahih_muslim_videos')
def Sahih_Muslim_Video_Page():
    return render_template('video_sahih_muslim.html')

@app.route('/fatwa_videos')
def Fatwa_Video_Page():
    return render_template('video_fatwa.html')

@app.route('/sahih_bukhari_videos')
def Sahih_Bukhari_Video_Page():
    return render_template('video_sahih_bukhari.html')

@app.route('/abu_dawoud_videos')
def Abu_Dawoud_Video_Page():
    return render_template('video_abu_dawoud.html')

@app.route('/sermons_videos')
def Sermons_Video_Page():
    return render_template('video_sermons.html')

@app.route('/lectures_videos')
def Lectures_Video_Page():
    return render_template('video_lectures.html')