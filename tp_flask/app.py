from flask import Flask
from CustomerDAO import CustomerDAO
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CustomerService(Resource):
    def get(self):
        data =[]
        customerDAO = CustomerDAO('data_full.csv')
        for customer in customerDAO.find_all():
            c = {'first_name':customer.first_name,'email':customer.email}
            data.append(c)
            
        return data

api.add_resource(CustomerService, '/')

if __name__ == '__main__':
    app.run(debug=True)



# @app.route("/hello")
# def hello_world():

#     customerDAO = CustomerDAO('data_full.csv')
#     out = "<table>"
#     for customer in customerDAO.find_all():
#         out+= f"""
#         <tr>
#         <td>{customer.first_name}</td>
#         <td>{customer.email}</td>
#         </tr>
#         """

#     out+= "</table>"
#     return out