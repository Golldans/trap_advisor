from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'trap_advisor'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'trap_advisor'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)
