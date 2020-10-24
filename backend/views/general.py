from flask import Blueprint

general = Blueprint('general', __name__)


@general.route('/')
def hello(user):
    return 'Hello'


@general.route('/reverse')
def about(user):
    return 'reverse'