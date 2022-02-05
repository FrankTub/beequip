from flask import Flask, request
from flask_restful import Resource, Api
from marshmallow import Schema, fields

from model import Customers, Installments, Leases

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'beequip.db'

class OutstandingLeaseAmountQuerySchema(Schema):
    reference = fields.Str(required=True)
    date = fields.Str(required=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

db = SQLAlchemy(app)
api = Api(app)

OutstandingLeaseAmountSchema = OutstandingLeaseAmountQuerySchema()

class OutstandingLeaseAmount(Resource):
    def get(self):
       errors = OutstandingLeaseAmountSchema.validate(request.args)
       if errors:
           return {'error': errors}, 400
       amt = db.session.query(Installments).join(Leases).filter(Leases.reference == request.args['reference']).filter(Installments.date == datetime.strptime(request.args['date'], '%Y-%m-%d')).with_entities(Installments.outstanding_start).all()
       #logging.error('%s raised an error', amt)
       if not amt:
           return {'error': ''}, 404 
       for row in amt:
           row_as_dict = dict(row)
       return {'OutstandingLeaseAmount': row_as_dict}, 200

api.add_resource(OutstandingLeaseAmount, '/outstandingleaseamount')

if __name__ == '__main__':  
    app.run()  # run our Flask app