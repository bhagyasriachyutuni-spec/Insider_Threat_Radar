from flask import Flask, render_template
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp

import os

app = Flask(__name__)

# ✅ SECRET KEY (more secure)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")

# ✅ OPTIONAL: Configurations (for future email feature)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['CSV_FOLDER'] = 'data'

# ✅ REGISTER BLUEPRINTS
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

# ✅ HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# ✅ OPTIONAL: Global Error Handling (good for production)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return "Something went wrong!", 500


if __name__ == "__main__":
    app.run(debug=True)