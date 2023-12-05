from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

PATH_TO_DB = "/Users/sowmyakarthikeyan/Desktop/db_course/research_assign/retail_app.db"

@app.route('/')

@app.route('/home')
def home():
    return render_template('home_page.html')

@app.route('/Customer', methods=['GET', 'POST'])
def Customer():
    return render_template('customer.html')

@app.route('/Add_Customer', methods=['GET', 'POST'])
def Add_Customer():
    return render_template('add_customer.html')

@app.route('/Form_Add_Customer', methods=['GET', 'POST'])
def Form_Add_Customer():
    if request.method == 'POST':
        customer_first_name = request.form.get('customer_first_name')
        customer_last_name = request.form.get('customer_last_name')
        customer_gender = request.form.get('customer_gender')
        customer_dob = request.form.get('customer_dob')

        conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(customer_id) FROM customer;")
        max_customer_id = cursor.fetchone()[0]

        if max_customer_id is None:
            customer_id = 1
        else:
            customer_id = max_customer_id + 1

        cursor.execute("INSERT INTO customer (customer_id, customer_first_name,\
                        customer_last_name, customer_gender, customer_dob)\
                        VALUES (?, ?, ?, ?, ?)", \
                       (customer_id, customer_first_name, customer_last_name, customer_gender,
                        customer_dob))

        conn.commit()
        conn.close() 

        return '<h1>Success!</h1> The customer record has been successfully added to the database.'
    else:
        return render_template('form_add_customer.html') 
    
@app.route('/Products', methods=['GET', 'POST'])
def Products():
    return render_template('product.html')

@app.route('/Get_Product', methods=['GET', 'POST'])
def Get_Product():
    return render_template('get_product.html')

@app.route('/form_get_product', methods=['GET', 'POST'])
def form_get_product():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        
        conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT * from product where product_id=?", (product_id,))
        product_info = cursor.fetchall()
        conn.close()

        return render_template('form_get_product.html', product_info=product_info)
    else:
        return render_template('form_get_product.html')


if __name__ == '__main__':
    app.run(debug=True)
