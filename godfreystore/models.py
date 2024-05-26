from . import db


class ProductDetail(db.Model):
    __tablename__ = 'product_detail'
    id = db.Column(db.Integer, primary_key=True)
    product_description = db.Column(db.String(25500), nullable=False)
    product_detail_image = db.Column(db.String(255), nullable=False)
    launch_date = db.Column(db.Date, nullable=False)
    bluetooth_support = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    made_in = db.Column(db.String(50), nullable=False)
    
    products = db.relationship('Product', backref='product_detail')

    def __repr__(self):
        return f"ID: {self.id}\nDescription: {self.product_description}\nLaunch Date: {self.launch_date}"

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    product_category = db.Column(db.String(50), nullable=False)
    stock_status = db.Column(db.String(20), nullable=False)
    product_detail_id = db.Column(db.Integer, db.ForeignKey('product_detail.id'), nullable=False)

    def __repr__(self):
        return f"ID: {self.id}\nName: {self.productname}\nPrice: ${self.price}\nCategory: {self.product_category}\nStock Status: {self.stock_status}"

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id',db.Integer,db.ForeignKey('products.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'product_id') )


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    shippingaddress = db.Column(db.String(500))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    products = db.relationship("Product", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        return f"ID: {self.id}\nStatus: {self.status}\nFirst Name: {self.first_name}\nSurname: {self.surname}\nEmail: {self.email}\nPhone: {self.phone}\nDate: {self.date}\nTours: {self.tours}\nTotal Cost: ${self.total_cost}"


