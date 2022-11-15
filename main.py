from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # обязательный ключ
    title = db.Column(db.String(100), nullable=False)  # нельзя установить пустое название
    intro = db.Column(db.String(300), nullable=False)  # нельзя создать статью у которой не будет вступительного текста
    text = db.Column(db.Text, nullable=False)  # нельзя создать пустую статью
    date = db.Column(db.DateTime, default=datetime.utcnow())  # если время не ввести то будет актуальное время

    def __repr__(self):
        return '<Article %r>' % self.id  # выдавать сам объект и его айди


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()  # сортировка ( desc от новых статей к старым )
    return render_template("posts.html", articles=articles)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)  # создаем объект

        try:
            db.session.add(article)  # добавляем объект
            db.session.commit()  # сохраняем объект
            return redirect('/posts')
        except:
            return "При добавлении статьи произошла ошибка!"
    else:
        return render_template("create-article.html")


@app.route('/posts/<int:id>')  # открываем статью на новой странице
def post_detail(id):
    article = Article.query.get(id)  # запрос к базе данных без сортировок
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')  # удаление
def post_delete(id):
    article = Article.query.get_or_404(id)  # выходит ошибка, если запись в базе данных не найдена

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении статьи произошла ошибка"


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])  # обновление изменных данных в статье
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()  # сохраняем объект
            return redirect('/posts')
        except:
            return "При редактировании статьи произошла ошибка!"
    else:
        return render_template("post_update.html", article=article)


# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return 'User page: ' + name + " - " + str(id)


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)  # показывать все ошибки на странице конечному пользователю


# создание бд
# from main import app, db
# app.app_context().push()
# db.create_all()
# или
# открываем flask shell, для этого в терминале пишем:
# flask shell
# >>>from app import db
# >>>db.create_all()