from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'test'
PASSWORD = 'mysql824.'

DA_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 指定使用的数据库
app.config['SQLALCHEMY_DATABASE_URI'] = DA_URI
# 跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建一个SQLAlchemy对象,需要放在config后面
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=True)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))


db.create_all()


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
    app.run()
