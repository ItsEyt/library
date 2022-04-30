from flask import Flask, redirect, render_template, request, url_for
from blueprints.admin import admin
from blueprints.user import user
from modules import filehelper as fh

api = Flask(__name__)
api.config['UPLOAD_FOLDER'] = fh.UPLOAD_FOLDER
api.register_blueprint(admin)
api.register_blueprint(user)

@api.route('/')
def home():
    user = request.args.get('name')
    if user == 'admin':
        return redirect(url_for("admin.admin_home"))
    elif user == 'user':
        return redirect(url_for("user.user_home"))
    return render_template('login.html')

# def main():
#     api.run()

# if __name__ == "__main__": main()
