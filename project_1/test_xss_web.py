from flask import Flask,session, render_template, request, redirect
import sqlite3
import os

sqliteConnection = sqlite3.connect('.\\project_1\\twist.sqlite', check_same_thread=False)
cursor = sqliteConnection.cursor()
folder = os.getcwd()
app  = Flask(__name__, static_folder=folder, template_folder=folder)
app.secret_key = 'hello'

@app.route('/search', methods=['GET', 'POST'])
def search_site():
    session['login'] = 'admin'
    if request.method == "GET" and request.args.get('qq'):
        a = request.args.get('qq')
        print(a)
        return f'''
                        <h1>Введите запрос поиска</h1>
                        <form action="/search" method="get">
                            <input type="text" name="qq">
                            <input type="submit" value="Отправить">
                        </form>
                        <h1>Вы ввели: {a}</h1>'''
    return '''
            <form action="/" method="get">
                <input type="text" name="qq">
                <input type="submit" value="Отправить">
            </form>
            <h1>Вы ввели: </h1>'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        query = "select login, password FROM users WHERE login ==  '" + login + "' and password =='" + password + "';"
        cursor.execute(query)
        result = cursor.fetchall()
        sqliteConnection.commit()
        if result != None and len(result) > 0:
            print('Результат',result)
            return redirect('/search')
    return '''
    <form action="/" method="post">
    <p>введите логин</p><input type="text" name="login">
    <p>введите пароль</p><input type="text" name="password"><br>
    <input type="submit" value="Войти">
    </form>
'''
    pass
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')