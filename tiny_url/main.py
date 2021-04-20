from .models import Url
from .models import CreateUrlInputSchema
from .utils  import save_url
from flask   import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

main = Blueprint('main', __name__)
create_url_schema = CreateUrlInputSchema()

@main.route('/')
def index():
    return "Hi! This is the homepage for TINYURL"


@main.route('/home')
@login_required
def home():
    return Url.query.filter_by(user_id=current_user.id)

@main.route('/new')
@login_required
def new_tiny_url():
    return render_template('tiny_url.html')

@main.route('/new', methods=['POST'])
@login_required
def new_tiny_url_post():
    errors = create_url_schema.validate(request.form)
    if errors: 
        abort(BAD_REQUSET, str(errors))

    save_url(request.form['original_url'])
        
    return redirect(url_for('main.index'))

@main.route('/<alias>', methods=['GET'])
def redirect_to_alias(alias):
	url_data = Url.query.filter_by(key=alias)
    if url_data is None:
        return bad_request('Unknown alias.')

    url = url_data["original_url"]
    
    return redirect(url, code=302)