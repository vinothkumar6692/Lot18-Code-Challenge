# -*- coding: utf-8 -*-
#
# @Author: Vinoth Kumar
# @Date:   2016-09-06
# @Email:  vinothkumar@nyu.edu


from flask import Flask, request, jsonify,render_template,url_for,g
import os 
from werkzeug import secure_filename
from modules import parser as order_parser
from modules import order_validator as validator1


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


########################################################
## REST ROUTES
########################################################

#Endpoint to import a csv file to the server
@app.route('/import/', methods= ['POST']) 
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.name)
            request.files['file'].save('static/uploads/orders.csv')
            validate_request('static/uploads/orders.csv')
            return jsonify(result={"status": 200, "message": "uploaded Sucessfully"})
        return jsonify(result={"status": 200, "message":"File Not uploaded"})

def validate_request(file):
    global JSONDATA
    JSONDATA = order_parser.parse(file)
    orders = JSONDATA['orders'][::-1]

    JSONDATA['orders'] = validator1.validate_orders(orders)

#Endpoint to retreive the orders information
@app.route('/orders', methods= ['GET'])
def get_orders():
    global JSONDATA
    valid = request.args.get("valid")
    if JSONDATA:
        newdata = []
        if valid:
            if valid == '1':
                for order in JSONDATA['orders']:
                    if order['valid'] == 1:
                        newdata.append(order)
                return jsonify(result={"status": 200, "message": "data sent", "data":newdata})
            elif valid == '0':
                for order in JSONDATA['orders']:
                    if order['valid'] == 0:
                        newdata.append(order)
                return jsonify(result={"status": 200, "message": "data sent", "data":newdata})
            else:
                return jsonify(result={"status": 200, "message": "Invalid option"})
        elif not request.args:
            return jsonify(result={"status": 200, "message": "data sent", "data":JSONDATA['orders']})
        else:
            return jsonify(result={"status": 200, "message": "invalid"})   
    else:
        return jsonify(result={"status": 200, "message": "orders not available"})   


#Endpoint to retrieve the information for a specific order
@app.route('/orders/<orderid>', methods= ['GET'])
def get_orderbyId(orderid):
    global JSONDATA
    if JSONDATA:
        for orders in JSONDATA['orders']:
            if orderid == orders['id']:
                return jsonify(result={"status": 200, "message": "data sent", "data":orders})
        return jsonify(result={"status": 200, "message": "Order Id not found", "data":None})
    else:
        return jsonify(result={"status": 200, "message": "orders not available"})

#Default Route
@app.route("/")
def hello():
	return render_template("index.html")


if __name__ == "__main__":
    global JSONDATA
    JSONDATA = {}
    app.debug = True
    app.run()