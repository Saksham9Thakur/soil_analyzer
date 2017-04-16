from flask import render_template, request,flash, redirect, url_for,session
import time
import serial
import string
from app import app, db
from app.models import *
import datetime 

import os,time
from itertools import cycle
@app.route('/' )
def index():
  return render_template('index.html')    

@app.route('/update' )
def update():
	rot13=string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	test=serial.Serial("/dev/ttyACMO",9600)
	time.sleep(4)
	line1=test.readline()
	line2=test.readline()
	line3=test.readline()
	db.session.add(Mitti(datetime.datetime.now(),line1,line2,line3,8))
	db.session.commit()
	return redirect(url_for('index'))   
