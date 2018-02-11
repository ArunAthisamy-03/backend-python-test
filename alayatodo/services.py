"""services.py holds the DAL of alayatodo app"""

from models import User, MyToDos
from alayatodo import db

class DBService():
    """
    Database service class to query database
    """

    #Get user name matching username and password
    def get_username(self, username, password ):
        """
        Validates username and password with database to return getUser result set
        :param username:
        :param password:
        :return: getUser
        """

        try:
            getUser = User.query.filter_by(username=username, password=password).first()
            return getUser

        except Exception as e:
            raise Exception("Exception while getting user name", e)


    #Get todolist by id
    def get_todo_by_id(self, id ):
        """
        Get todo list by id and return todo result set
        :param id:
        :return: todo
        """

        try:
            todo = MyToDos.query.filter_by(id=id).first()
            return todo

        except Exception as e:
            raise Exception("Exception while getting todo by id", e)


    #Convert resultset to dictionary
    def convert_todo_dict(self, todo ):
        """
        convert todo result set to dictionary
        :param todo:
        :return: todo_dict
        """

        try:
            todo_dict = MyToDos.to_dict(todo)
            return todo_dict

        except Exception as e:
            raise Exception("Exception while converting todo result set in to dictionary", e)


    #Get all todoitems
    def getalltodo(self):
        """
        Get all the todo item from database and return to views
        :return: todos
        """

        try:
            todos = MyToDos.query.all()
            return todos

        except Exception as e:
            raise Exception("Exception while getting entire todo list", e)


    #Add item to todolist
    def addtodoitem(self,user_id, description, is_completed):
        """
        Add an item to database todo list
        :param user_id:
        :param description:
        :param is_completed:
        :return: void
        """

        try:
            addtodo = MyToDos(user_id = user_id, description = description,is_completed = is_completed)
            db.session.add(addtodo)
            db.session.commit()

        except Exception as e:
            raise Exception("Exception while adding an item to todo list", e)


    #Delete item from the todolist
    def deletetodoitem(self,id):
        """
        Delete an item from todo list
        :param id:
        :return: void
        """

        try:
            deleteTodo = MyToDos.query.get(id)
            db.session.delete(deleteTodo)
            db.session.commit()

        except Exception as e:
            raise Exception("Exception while deleting an item to todo list", e)


    #Update an item in the todolist
    def updatetodoitem(self, id, is_checked):
        """
        Update an item in the todo list
        :param id:
        :param is_checked:
        :return: void
        """

        try:
            getUser = MyToDos.query.filter_by(id=id).first()
            getUser.is_completed = is_checked
            db.session.commit()

        except Exception as e:
            raise Exception("Exception while deleting an item to todo list", e)








