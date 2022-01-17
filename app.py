from flask import Flask
from flask_migrate import Migrate

import config
from extension import db
from models import Article, User, UserExtension

app = Flask(__name__)
app.config.from_object(config)

# 创建一个SQLAlchemy对象,需要放在config后面
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/otm')
def one_to_many():
    article1 = Article(title='1', content='1')
    article2 = Article(title='2', content='2')
    user = User(username='alin')
    article1.author = user
    article2.author = user
    db.session.add(article1, article2)
    print(user.articles)
    db.session.commit()
    return 'otm success！'


@app.route('/oto')
def one_to_one():
    user = User.query.filter_by(id=1)[0]
    extension = UserExtension(school="Swust")
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return "one to one"


@app.route("/article")
def article_view():
    # 1、添加数据
    # article = Article(title="1", content='ok')
    # db.session.add(article)
    # db.session.commit()

    # 2.查询数据
    # article = Article.query.filter_by(id=1)[0]
    # print(article.content)

    # 3.修改数据
    # article = Article.query.filter_by(id=1)[0]
    # article.content = 'okkkkkkkk'
    # db.session.commit()

    # 4、删除数据
    Article.query.filter_by(id=1).delete()
    db.session.commit()
    return "success"


@app.route('/')
def test():
    engine = db.get_engine()

    with engine.connect() as conn:
        result = conn.execute('select 1')
        print(result.fetchone())
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
