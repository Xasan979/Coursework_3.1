from flask import Blueprint, render_template, request



error_pages_blueprint = Blueprint('errors', __name__, template_folder="templates")

@error_pages_blueprint.app_errorhandler(404)
def handle_404(err):
    return render_template('error.html', er_code=404), 404

@error_pages_blueprint.app_errorhandler(500)
def handle_500(err):
    return render_template('error.html', er_code=500), 500