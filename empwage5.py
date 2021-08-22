from flask import Flask, request, jsonify
import random

app = Flask(__name__)

data = [{'id': 1, 'name': 'Anusha', 'no_of_working_days': 0, 'attendance':0 ,'salary': 0}, {
        'id': 2, 'name': 'nikita', 'no_of_working_days': 0, 'attendance': 0, 'salary': 0},
         {'id': 3, 'name': 'sanket', 'no_of_working_days': 0, 'attendance': 0, 'salary': 0}]
EMP_WAGE_PER_HR=20

class EmployeeWage:


    def __init__(self, data):
        self.data = data
     

    @app.route('/')
    def hello():
        return 'welcome to Employee Wage Program'

    @app.route('/employee_data')    
    def employee_database():
        return jsonify({'data': data})

    @app.route('/employee_data/<int:id>')
    def employee(id):
        employee = [emp['name'] for emp in data if emp['id'] == id]
        return jsonify({id : employee})

    @app.route('/attendance/<int:id>')
    def attendance_status(id):
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
        emp_rand = random.randint(1,2)
        if emp_rand == 1:
            emp_hours=8
        else:
            emp_hours = 4
        return emp_hours 
    @app.route('/employee_data/add_emp', methods = ['POST'] )
    def add_emp():
        req_data = request.get_json()

        new_emp = {'id':req_data['id'], 'name':req_data['name'], 'no_of_working_days': 0, 'attendance':0 ,'salary': 0}
        data.append(new_emp)
        return jsonify({'added': new_emp})

    @app.route('/employee_data/delete/<int:id>', methods = ['DELETE'])
    def delete(id):
        new_data = data.pop(id-1)
        return jsonify({'removed_emp_data': new_data})
    @app.route('/employee_data/update/<int:id>', methods = ['PUT'])
    def update(id):
        for employe in data:
            if employe['id'] == id:
                req_data= request.get_json()
                employe['name'] = req_data["name"]
                return jsonify({'updated': employe})






if __name__ == '__main__':
    app.run(port= 7420, debug= True)
