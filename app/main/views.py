import os
from flask import render_template,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Role,Comment,Pitch
from .. import db
from manage import app

@main.route('/')
def index():

    title = 'Pitches | Hub'
  
    return render_template('index.html',title=title)