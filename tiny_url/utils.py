# coding:utf-8
from . import db
from .models import Url
from urllib.parse import urlparse
import string
import random


def generate_url_id():
    lst = [random.choice(string.ascii_letters + string.digits) for n in range(7)]
    url_id = "".join(lst)

    return url_id

def save_url(original_url):
    url_id = generate_url_id()

    shorten_url = Url(key=url_id, original_url=original_url, user_id=current_user)

    try:
        db.session.add(url)
        db.session.commit()
    except Error as err:
        raise err.message

    return None 