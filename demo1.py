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

    # 外键
    # 1、外键的数据类型与所引用的键的类型一致
    # 2、db.ForeignKey(表名.字段)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # relationship
    # 1、第一个参数和模型绑定
    # 2、backref(back reference): 反向引用，代表对方访问我的时候的字段名称
    author = db.relationship('User', backref="articles")


# 若新建关系，则先drop掉之前建立的表
db.drop_all()

db.create_all()


@app.route('/otm')
def one_to_many():
    article1 = Article(title='1', content='1')
    article2 = Article(title='2', content='2')
    user = User(username='alin')
    article1.author = user
    article2.author = user
    db.session.add(article1, article2)
    db.session.commit()
    return 'otm success！'


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
