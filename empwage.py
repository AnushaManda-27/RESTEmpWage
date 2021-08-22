import re
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

data = [{'id': 1, 'name': 'Anusha'}, {
        'id': 2, 'name': 'nikita'}, {'id': 3, 'name': 'sanket'}]


class EmployeeWage:

    def __init__(self, data):
        self.data = data

    @app.route('/')
    def hello():
        return 'welcome to Employee Wage Program'

    @app.route('/employee_data/')
    def employee_database():
        return jsonify({'data': data})

    @app.route('/employee_data/<int:id>')
    def employee(id):
        employee = [emp['name'] for emp in data if emp['id'] == id]
        return jsonify({id: employee})

    @app.route('/attendance/<emp>')
    def attendance(emp):
        emp_check = random.randint(0, 1)
        if emp_check == 1:
            status = 'present'
            return jsonify({emp: status})
        return None

    @app.route('/employee_data/delete/<emp>')
    def delete(emp):
        new_data = data.pop(emp)
        return jsonify({'new_data': new_data})

    


if __name__ == '__main__':
    app.run(port=7500, debug=True)
