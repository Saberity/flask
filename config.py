# 配置数据库
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'test'
PASSWORD = 'mysql824.'

DA_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 指定使用的数据库
SQLALCHEMY_DATABASE_URI = DA_URI
# 跟踪数据库的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
