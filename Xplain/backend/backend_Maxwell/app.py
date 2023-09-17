from flask import Flask
from routes.questions import questions
from database.database import db

app = Flask(__name__)
app.register_blueprint(questions)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'test'
db.init_app(app)

if __name__ == '__main__':
    app.run()