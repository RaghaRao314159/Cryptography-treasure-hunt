#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:22:15 2022

@author: Ragha
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def main_page():
    if request.form.get('stage1'):
        global bool1
        bool1 = (lambda x: "CORRECT" if (request.form.get('stage1') == "Initial:a_4,Final:a_18") else "WRONG")(3)
        return redirect(url_for('stage_1'))
    
    elif request.form.get('stage2'):
        global bool2
        bool2 = (lambda x: "CORRECT" if (request.form.get('stage2') == "[4,3,2,1,26,18,26,24,16,15,14,13,18]") else "WRONG")(3)
        return redirect(url_for('stage_2'))
    
    elif request.form.get('stage3'):
        global bool3
        bool3 = (lambda x: "CORRECT" if (request.form.get('stage3') == "To any recruit that picks up this canteen, immediately DROP 20!") else "WRONG")(3)
        return redirect(url_for('stage_3'))
    
    elif request.form.get('stage4'):
        global bool4
        bool4 = (lambda x: "CORRECT" if (request.form.get('stage4') == "bR0ncODe") else "WRONG")(3)
        return redirect(url_for('stage_4'))
    
    else: 
        return render_template('main_page.html')
    





@app.route('/stage_1',methods=['POST','GET'])
def stage_1():
    if request.form.get('back'):
        return redirect(url_for('main_page'))
    else:
        return render_template('stage_1.html', bool1 = bool1)
    
    
@app.route('/stage_2',methods=['POST','GET'])
def stage_2():
    if request.form.get('back'):
        return redirect(url_for('main_page'))
    else:
        return render_template('stage_2.html', bool2 = bool2)
    
@app.route('/stage_3',methods=['POST','GET'])
def stage_3():
    if request.form.get('back'):
        return redirect(url_for('main_page'))
    else:
        return render_template('stage_3.html', bool3 = bool3)

@app.route('/stage_4',methods=['POST','GET'])
def stage_4():
    if request.form.get('back'):
        return redirect(url_for('main_page'))
    else:
        return render_template('stage_4.html', bool4 = bool4)


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    