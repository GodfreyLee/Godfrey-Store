from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import ProductDetail, Product, Order, orderdetails
from datetime import datetime
from .forms import CheckoutForm
from . import db




main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    products = db.session.scalars(db.select(Product).order_by(Product.id)).all()
    return render_template('index.html', products=products)


# View the product detail page
@main_bp.route('/item/<int:product_id>')
def item(product_id):
    product = db.session.query(Product).get(product_id)
    return render_template('item.html', product=product)

# Search Result
@main_bp.route('/search')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    product = Product.query.filter(Product.productname.like(search)).all()
    return render_template('search.html', product=product )

# Referred to as "Basket" to the user
@main_bp.route('/order', methods=['POST', 'GET'])
def order():
    product_id = request.values.get('product_id')
    print(f'Values: {product_id}')
    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        # order will be None if order_id/session is stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('Failed trying to create a new order!')
            order = None
    
    # calculate total price
    total_price = 0
    if order is not None:
        for product in order.products:
            total_price += product.price
    
    # are we adding an item?
    if product_id is not None and order is not None:
        product = db.session.scalar(db.select(Product).where(Product.id==product_id))
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                flash('There was an issue adding the item to your basket',category='danger')
            return redirect(url_for('main.order'))
        else:
            flash('There is already one of these in the basket')
            return redirect(url_for('main.order'))
    return render_template('order.html', order=order, total_price=total_price)

# Delete specific basket items
# Note this route cannot accept GET requests now
@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = db.get_or_404(Order, session['order_id'])
        product_to_delete = db.session.scalar(db.select(Product).where(Product.id==id))
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# Scrap basket
@main_bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

# Complete the order
@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = db.get_or_404(Order, session['order_id'])
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.shippingaddress = form.shippingaddress.data
            total_cost = 0
            for product in order.products:
                total_cost += product.price
            order.totalcost = total_cost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! One of our team members will contact you soon...')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)
