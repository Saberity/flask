from extension import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(20), nullable=False)


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


# 与User一对一关系
class UserExtension(db.Model):
    __tablename__ = 'user_extension'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # db.backref
    # 1、在反向引用的时候，如果需要传递其他参数，则需要使用
    # 2、uselist=False：表示反向引用的时候，不是一个列表，而是一个对象
    user = db.relationship('User', backref=db.backref('extension', uselist=False))
