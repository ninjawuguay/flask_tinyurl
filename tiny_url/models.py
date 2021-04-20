# coding:utf-8
from datetime import datetime
from . import db 
from marshmallow import Schema, fields, validates, ValidationError


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     name = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     urls = db.relationship('Url', backref='author', lazy=True)


class Url(db.Model):
    __tablename__ = 'urls'
    key = db.Column(db.String(7), primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    clicks = db.Column(db.Integer, nullable=False, default=0)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class CreateUrlInputSchema(Schema):
    original_url = fields.URL(required=True)
