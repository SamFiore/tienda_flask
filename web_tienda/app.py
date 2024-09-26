from flask import Flask,render_template,request,redirect,url_for
from flask_migrate import Migrate
from dotenv import load_dotenv
from database import db
from models import Article
from forms import ArticleFrom
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

user_db = os.getenv('USER')
psw_db = os.getenv('PSW')
name_db = os.getenv('DB')
url_db = os.getenv('HOST')
port_db = os.getenv('PORT')

FULL_URL_DB = f'postgresql://{user_db}:{psw_db}@{url_db}:{port_db}/{name_db}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app,db)

@app.route('/',methods=['GET','POST'])
def start():
    article=Article()
    articleForm=ArticleFrom(obj=article)
    articles = article.query.order_by('id')
    if request.method == 'POST':
        if articleForm.validate_on_submit():
            articleForm.populate_obj(article)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('start'))
    return render_template('index.html',forma=articleForm,articles=articles)

@app.route('/edit/<int:id>',methods=['POST','GET'])
def edit(id):
    article = Article.query.get_or_404(id)
    articleForm = ArticleFrom(obj=article)
    articles = Article.query.order_by('id')
    if request.method == 'POST':
        if articleForm.validate_on_submit():
            articleForm.populate_obj(article)
            db.session.commit()
            return redirect(url_for('start'))
    return render_template('index.html',forma=articleForm,articles=articles,flagEdit=True,idArt=id)

@app.route('/delete/<int:id>')
def delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('start'))

if __name__ == '__main__':
    app.run(debug=True)