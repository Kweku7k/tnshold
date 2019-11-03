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
    vendor = db.Column(db.String(50))

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
        order_vendor = request.form['vendor']

        identify = Order.id
        final_order = Order(name=order_name, pNumber=order_pnumber, room=order_room, aNumber=order_anumber, food=order_food, hostel=order_hostel, block=order_block, total=order_total, vendor=order_vendor)
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
    all_orders = Order.query.order_by(Order.date_created).all()
    return render_template('chart.html', all_orders=all_orders)

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

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    order_to_delete = Order.query.get_or_404(id)

    # try:
    db.session.delete(order_to_delete)
    db.session.commit()
#    return render_template('delivery')
    return redirect('/deliveryportal')
    # except:
        # return 'There was a problem deleting that order'



@app.route('/delivery')
def delivery():
    # if request.method == 'POST':
    #     vendor = request.form['username'] 
    #     password = request.form['password']
    #     if (vendor === "Kweku" || password === "Aloo")
    #     {
    #         return redirect('deliveryportal.html')
    #     }
    #     else:
    #         return ("Sorry, that didnt work...")

    # }
    # else{
    return render_template('delivery.html')

    # }, all_orders=all_orders
# --------------------vendors-----------------------
@app.route('/anything', methods=['POST','GET'])
def anything():
    return render_template('anything.html')

@app.route('/hotoven', methods=['POST','GET'])
def hotoven():
    return render_template('hotoven.html')

@app.route('/indomiebar', methods=['POST','GET'])
def indomiebar():
    return render_template('indomiebar.html')

@app.route('/spectra', methods=['POST','GET'])
def spectra():
    return render_template('spectra.html')


@app.route('/deliveryportal', methods=['POST','GET'])
def deliveryportal():   
    if request.method == 'POST':
        vendor = request.form['username'] 
        password = request.form['password']
        TNS = "Kweku"
        TNSpass = "123"
        Shawarma ="Sha"
        ShawarmaPass = "Sha"
        Sobolo = "Nana Esi"
        SoboloPass = "SOBOLO"
        # anything
        anything = "niijunior120@gmail.com"
        anythingPass = "anypassword"
        # The Indomie Bar
        indomiebar = "claudiaboateng8@gmail.com"
        indomiePass = "claudia07"
        # Spectra's Kitchen
        spectra = "specsforlife590@gmail.com"
        spectraPass = "Dreamers"



        if vendor == TNS and password == TNSpass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.order_by(Order.id).all()
            return render_template('deliveryportal.html', all_orders=all_orders)
    
        elif vendor == Shawarma and password == ShawarmaPass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.filter_by(vendor = "Test Vendor 1").all()
            return render_template('deliveryportal.html', all_orders=all_orders)


        elif vendor == Sobolo and password == SoboloPass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.filter_by(vendor = "Test Vendor 2").all()
            return render_template('deliveryportal.html', all_orders=all_orders)

        elif vendor == anything and password == anythingPass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.filter_by(vendor = "Test Vendor 2").all()
            return render_template('deliveryportal.html', all_orders=all_orders)
        
        elif vendor == indomiebar and password == indomiePass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.filter_by(vendor = "The Indomie Bar").all()
            return render_template('deliveryportal.html', all_orders=all_orders)
        
        elif vendor == spectra and password == spectraPass:
            # all_orders = Order.query.order_by(Order.id).all()
            all_orders = Order.query.filter_by(vendor = "Spectra's Kitchen").all()
            return render_template('deliveryportal.html', all_orders=all_orders)

        
        else:
            return ("Sorry, that didnt work...")

    
    else:
        # all_orders = Order.query.order_by(Order.date_created).all()
        # return ('Sorry, epic system failure. Please contact administrator on 0545977791')
        return render_template('deliveryportal.html', )

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
        return render_template('final.html', all_issues=all_issues )

    else:
        return "Sorry, didnt work..."


@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/ourvendors')
def ourvendors():
    return render_template('vendors.html')


if __name__ == "__main__":
    app.run(debug=True)