from flask import Flask
from extensions import db
from books.routes import books_bp
from models import Book



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(books_bp, url_prefix="/books")

    with app.app_context():
        db.create_all()

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)