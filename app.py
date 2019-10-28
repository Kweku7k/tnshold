from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    room = db.Column(db.Integer)
    pNumber = db.Column(db.String(10))
    aNumber = db.Column(db.String(10))
    hostel = db.Column(db.String(100))
    food = db.Column(db.String(1000))
    quantity = db.Column(db.Integer)
    status = db.Column(db.Integer)
    block = db.Column(db.String(100))
    total = db.Column(db.String(10))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Order %r>' % self.name


class Complaints(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(20))
    c_number = db.Column(db.String(20))
    c_complaints = db.Column(db.String(200))
    
    def __repr__(self):
        return '<Complaint %r>' %self.c_name

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/menu', methods=['POST','GET'])
def menu():
    return render_template('menu.html')
    # if request.method == 'POST':
    #     order_food = request.f <!-- <input type="textarea" sty <!-- <input type="textarea" style="height: 130px; resize: none;" class="form-control" id="phone"> -->le="height: 130px; resize: none;" class="form-control" id="phone"> -->orm['food']
    #     cho = Order(food=order_food)
    #     print (cho)
    #     db.session.add(cho)
    #     db.session.commit()

@app.route('/move', methods=['POST','GET'])
def move():
     if request.method == 'POST':
        order_food = request.form['food']
        cho = Order(food=order_food)
        print (cho)
        db.session.add(cho)
        # db.session.commit()
        return render_template('test.html', cho=cho)


@app.route('/test', methods=['POST','GET'])
def index():
    if request.method == 'POST' :
        # order_id = request.form['id']
        order_name = request.form['Name']
        order_room = request.form['Room']
        order_pnumber = request.form['phone']
        order_anumber = request.form['aphone']
        order_food = request.form['food']
        order_hostel = request.form['hostel']
        order_block = request.form['block']
        order_total = request.form['total']

        identify = Order.id
        final_order = Order(name=order_name, pNumber=order_pnumber, room=order_room, aNumber=order_anumber, food=order_food, hostel=order_hostel, block=order_block, total=order_total)
        # user_number = Order(pNumber=order_pnumber)
        # user_room = Order(room=order_room)
        # order_anumber = request.form['aphone']
        # user_anumber = Order(aNumber=order_anumber)

        # print('request form: {}'.format(request.form))

        # try :
        db.session.add(final_order)
        db.session.commit()
        all_orders = Order.query.order_by(Order.date_created).all()
        print (all_orders)
        print (identify)
        return render_template('invoice.html', all_orders=all_orders )

        # return render_template('invoice.html', )

        # except Exception as e:
        #     print(e)
        #     return "There was an issue adding your order"

    else:
        all_orders = Order.query.order_by(Order.date_created).all()
        return render_template('index.html', all_orders=all_orders)
 
   
@app.route('/chart', methods=['POST','GET'])
def masterchart():
    return ('chart.html')

@app.route('/new')
def new():
    return render_template('test.html')

@app.route('/vendor')
def vendor():
    return render_template('vendor.html')

@app.route('/vendors')
def vendors():
    all_orders = Order.query.order_by(Order.date_created).all()
    return render_template('vendorportal.html', all_orders=all_orders)

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/deliveryportal')
def deliveryportal():
    all_orders = Order.query.order_by(Order.date_created).all()
    return render_template('deliveryportal.html', all_orders=all_orders)

@app.route('/reply')
def reply():
    return render_template('reply.html')



@app.route('/complaints', methods=['POST','GET'])
def complaints():
    if request.method == 'POST' :
        issue_name = request.form['com_name']
        issue_number = request.form['com_number']
        issue_complaint = request.form['com_complaints']

        issue = Complaints(c_name=issue_name, c_number=issue_number, c_complaints = issue_complaint)
        
        db.session.add(issue)
        db.session.commit()
        all_issues = Complaints.query.all()
        print (all_issues)
        return render_template('issues.html', all_issues=all_issues )

    else:
        return "Sorry, didnt work..."


@app.route('/invoice')
def invoice():
    return render_template('invoice.html')


if __name__ == "__main__":
    app.run(debug=True)