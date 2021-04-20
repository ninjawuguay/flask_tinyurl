from flask import Blueprint, render_template 

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
	return "this page will be used to signup users"

@auth.route('/login')
def login():
	return "This page will be used to login users"

@auth.route('/logout')
def logout():
	return "Use this to logout"
