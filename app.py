from flask import Flask, render_template
from database import init_db
from recipes.controller import recipes
from regions.controller import regions
from auth.controller import auth
from users.controller import users

init_db()
app = Flask(__name__)
app.secret_key = '126456653531-lj5rtfrsc6vfnto3aqimu68ehg4ilhmj.apps.googleusercontent.com'

# Register all the blueprints
app.register_blueprint(recipes)
app.register_blueprint(regions)
app.register_blueprint(auth)
app.register_blueprint(users)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
