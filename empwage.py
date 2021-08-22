
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

data = [{'id': 1, 'name': 'Anusha', 'no_of_working_days': 0, 'attendance':0 ,'salary': 0}, {
        'id': 2, 'name': 'nikita', 'no_of_working_days': 0, 'attendance': 0, 'salary': 0},
         {'id': 3, 'name': 'sanket', 'no_of_working_days': 0, 'attendance': 0, 'salary': 0}]
EMP_WAGE_PER_HR=20

class EmployeeWage:

    '''Class: Employewage class is created to do curd operations on  employee data
        parameters: data
        '''


    def __init__(self, data):
        self.data = data
     

    @app.route('/')
    def hello():
        '''Function: hello() is defined to display
        '''
        return 'welcome to Employee Wage Program'

    @app.route('/employee_data/')   
    def employee_database():
        '''Function: employee_database() id defined to jsonify to employee data
            Return: data'''
        return jsonify({'data': data})

    @app.route('/employee_data/<int:id>')
    def employee(id):
        '''Function: employee() takes id as arguments to get name if particular id of employee
            Arguments: id
            Return: jsonify({id : employee})'''
        employee = [emp['name'] for emp in data if emp['id'] == id]
        return jsonify({id : employee})

    @app.route('/attendance/<int:id>')
    def attendance_status(id):
        '''Function: attendance_status() takes id as arguments to get attendance if particular id of employee
            Arguments: id
            Return: jsonify({'employee' : employee})'''

        for employe in data:
            if employe['id'] == id:
                emp_check = random.randint(0, 1)
                if emp_check == 1:
                    employe['attendance'] = 1
                    employe['no_of_working_days'] += 1
                    work_hrs = EmployeeWage.emp_hrs()
                    employe['salary'] += work_hrs * EMP_WAGE_PER_HR
                    return jsonify({'employe': employe})
                else:
                
                    employe['attendance'] = 0
            
                    return jsonify({'employe': employe})

    def emp_hrs():
        '''Function: emp_hrs() is defined to get randomly generated employee work hours 
            Arguments: None
            Return: emp_hours'''
        emp_rand = random.randint(1,2)
        if emp_rand == 1:
            emp_hours=8
        else:
            emp_hours = 4
        return emp_hours 

        

    @app.route('/employee_data/delete/<emp>')
    def delete(emp):
        '''Function: delete() takes emp as arguments to delete particular employee by giving their id
            Arguments: emp
            Return: jsonify({'new_data': new_data})'''
        new_data = data.pop(emp)
        return jsonify({'new_data': new_data})



if __name__ == '__main__':
    app.run(port= 7500, debug= True)
