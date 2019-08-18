from flask import request
from flask_restplus import Resource

from ..util.dto import TodoDto
from ..service.todo_service import insert_todo, get_todos, get_a_todo, delete_todo, update_todo

api = TodoDto.api
_todo = TodoDto.todo

"""
flask-restplus examples : https://flask-restplus.readthedocs.io/en/stable/example.html
"""

@api.route('/')
class TodoList(Resource):
    @api.doc('list_of_registered_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        return get_todos()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_todo, validate=True)
    def post(self):
        data = request.json
        return insert_todo(data=data)

@api.route('/<id>')
@api.param('id', 'The todo identifier')
@api.response(404, 'todo found.')
class Todo(Resource):
    @api.doc('get a todo')
    @api.marshal_with(_todo)
    def get(self, id):
        todo = get_a_todo(id)
        if not todo:
            api.abort(404)
        else:
            return todo

    @api.doc('delete a user')
    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        delete_todo(id)
        return '', 204

    @api.doc('get a todo')
    @api.response(201, 'User successfully updated.')
    @api.expect(_todo, validate=True)
    def put(self, id):
        data = request.json

        return update_todo(id, data), 201