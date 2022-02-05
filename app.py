from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Customers(Resource):
    # methods go here
    def get(self):
        data = pd.read_csv('data\customers.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
    
class Installments(Resource):
    def get(self):
        data = pd.read_csv('data\installments.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

class Leases(Resource):
    def get(self):
        data = pd.read_csv('data\leases.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

api.add_resource(Customers, '/customers')  # '/customers' is our entry point for Customers
api.add_resource(Installments, '/installments')  # and '/installments' is our entry point for Installments
api.add_resource(Leases, '/leases')  # and '/leases' is our entry point for Leases

if __name__ == '__main__':
    app.run()  # run our Flask app