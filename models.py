import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import faker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

app = Flask("lycaeum")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kmsmjnwvsbqhex:6ff9187d0d347ceb49077c99012ca87866568c06a45a68e0d72f354d15ca3cd6@ec2-52-73-247-67.compute-1.amazonaws.com:5432/dcmvtertc2vrsd'
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = "invoice_customer"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    jdate = db.Column(db.Date)
    address = db.Column(db.String)
    email = db.Column(db.String)
    invoices = db.relationship('Invoice', backref="customer")

class Invoice(db.Model):
    __tablename__ = "invoice_invoice"
    id = db.Column(db.Integer, primary_key = True)
    particulars = db.Column(db.String)
    date = db.Column(db.Date)
    amount = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('invoice_customer.id'))

def create_db():
    db.create_all()

def main():
    create_db()
    f = faker.Faker()
    session = db.session
    for i in range(100):
        c = Customer(name = f.name(),
                     jdate = f.date(),
                     address = f.address(),
                     email = f.email())
        session.add(c)
        for j in range(5):
            invoice = Invoice(particulars = f.sentence(),
                              date = f.date(),
                              amount = random.randint(10, 99),
                              customer = c)
            session.add(invoice)
    session.commit()
                              
    



if __name__ == "__main__":
    main()
