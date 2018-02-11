""" Models of SQLAlchemy ORM  """
from flask_sqlalchemy import SQLAlchemy


# create a new SQLAlchemy object
db = SQLAlchemy()



# model class for users data table
class User(db.Model):
    """ Class to hold properties of users data table """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


    # function to convert result object to dictionary
    def to_dict(model_instance, query_instance=None):
        """
        Function to convert SQLALCHEMY users table result objects to dictionary
        :param query_instance:
        :return: dictionary
        """

        if hasattr(model_instance, '__table__'):
            return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
        else:
            cols = query_instance.column_descriptions
            return {cols[i]['name']: model_instance[i] for i in range(len(cols))}


    # function to represent values of users table
    def __repr__(self):
        """
        Built-in function to represent values of users table
        :return:
        """

        return '<User %r>' % self.id, self.username, self.password



# model class for todos data table
class MyToDos(db.Model):
    """Class to hold properties of todos data table"""

    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    description = db.Column(db.String(255))
    is_completed = db.Column(db.Boolean)


    # function to convert result object to dictionary
    def to_dict(model_instance, query_instance=None):
        """
        Function to convert SQLALCHEMY todos table result objects to dictionary
        :param query_instance:
        :return: dictionary
        """

        if hasattr(model_instance, '__table__'):
            return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
        else:
            cols = query_instance.column_descriptions
            return {cols[i]['name']: model_instance[i] for i in range(len(cols))}


    # function to represent values of todos table
    def __repr__(self):
        """
        Built-in function to represent values of todos table
        :return: void
        """

        return '<Todo %r>' % self.id, self.user_id, self.description, self.is_completed

