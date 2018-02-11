"""views.py holds the business logic of alayatodo app"""

from alayatodo import app,logger
from services import DBService
from flask import (
    redirect,
    render_template,
    request,
    session,
    )
import json

#Global variables
added = False
deleted = False
mark_as_complete = False
db_service = DBService()


# home method of alayatodo app
@app.route('/')
def home():
    """Home method called when the application is initialized"""

    with app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l.decode('utf-8') for l in f)
        return render_template('index.html', readme=readme)


# get method for login page
@app.route('/login', methods=['GET'])
def login():
    """
    Login GET method is used to fetch login page
    :return: renders login.html page
    """

    return render_template('login.html')


# post method for login page
@app.route('/login', methods=['POST'])
def login_POST():
    """
    Login POST method is used to post and validate user
    :return: void
    """

    try:
        username = request.form.get('username')
        password = request.form.get('password')
        getUser = db_service.get_username(username, password)
        if getUser:
            session['user'] = getUser.id
            session['logged_in'] = True
            return redirect('/todo')

    except Exception as e:
        logger.error(e)
        return redirect('/error')

    return redirect('/login')


# logout method to logout an existing user
@app.route('/logout')
def logout():
    """
    Log out method is used to implement log out functionality
    :return: void
    """

    try:
        session.pop('logged_in', None)
        session.pop('user', None)
        return redirect('/')

    except Exception as e:
        logger.error(e)
        return redirect('/error')



# method to get todos details of a selected item
@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    """
    TODO GET method is used to fetch details of a selected item
    :param id: int
    :return: void
    """

    try:
        todo = db_service.get_todo_by_id(id)
        todo_dict = db_service.convert_todo_dict(todo)
        return render_template('todo.html', todo=todo_dict)

    except Exception as e:
        logger.error(e)
        return redirect('/error')


# method to get todos details of a selected item in json format
@app.route('/todo/<id>/json', methods=['GET'])
def todojson(id):
    """
    Todo json GET method is used to fetch details of a selected item in json format
    :param id: int
    :return: todo
    """

    try:
        todos = db_service.get_todo_by_id(id)
        todos_dict = db_service.convert_todo_dict(todos)
        todos_json = json.dumps(todos_dict)
        return render_template('json.html', todo=todos_json)

    except Exception as e:
        logger.error(e)
        return redirect('/error')


# todos method to get information of all items
@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todos():
    """
    Todos GET method used to fetch list of items todo
    :return: todos, msg
    """

    try:
        global added
        global deleted
        global mark_as_complete
        messageList = []
        if not session.get('logged_in'):
            return redirect('/login')
        todos = db_service.getalltodo()
        messageList.append(added)
        messageList.append(deleted)
        messageList.append(mark_as_complete)
        added = False
        deleted = False
        mark_as_complete = False
        return render_template('todos.html', todos=todos, msg = messageList)

    except Exception as e:
        logger.error(e)
        return redirect('/error')


# todos post method to add a new item to todolist
@app.route('/todo', methods=['POST'])
@app.route('/todo/', methods=['POST'])
def todos_POST():
    """
    Todos POST used to add new item to todolist
    :return: void
    """

    try:
        global added
        if not session.get('logged_in'):
            return redirect('/login')
        user_id = session['user']
        description = request.form.get('description', '')
        is_completed = False
        db_service.addtodoitem(user_id,description,is_completed)
        added = True
        return redirect('/todo')

    except Exception as e:
        added = False
        logger.error(e)
        return redirect('/error')


# todo_delete method to delete a selected item from todolist
@app.route('/todo/<id>', methods=['POST'])
def todo_delete(id):
    """
    Todo_delete POST used to delete an existing item from todolist
    :param id: int
    :return: void
    """

    try:
        global deleted
        if not session.get('logged_in'):
            return redirect('/login')
        db_service.deletetodoitem(id)
        deleted = True
        return redirect('/todo')

    except Exception as e:
        deleted = False
        logger.error(e)
        return redirect('/error')


# todochk method used to mark an item in the list to complete
@app.route('/todochk', methods=['POST'])
def todochk_POST():
    """
    Todochk method used to mark an item in the list to complete
    :return: void
    """

    try:
        global mark_as_complete
        if not session.get('logged_in'):
            return redirect('/login')
        id = request.form['id']
        is_checked = str_to_bool(request.form['isChecked'])
        db_service.updatetodoitem(id,is_checked)
        mark_as_complete = True

    except Exception as e:
        mark_as_complete = False
        logger.error(e)
    return redirect('/todo')


# method to render genric error page
@app.route('/error')
def error():
    """
    Error method to render error page when there is an exception
    :return: void
    """

    return render_template('error.html')


# method to convert string to boolean
def str_to_bool(str_val):
    """
    str_to_bool method is used to convert string to boolean
    :param str_val:
    :return: Bool
    """

    if str_val == 'true':
         return True
    elif str_val == 'false':
         return False
    else:
         raise ValueError
