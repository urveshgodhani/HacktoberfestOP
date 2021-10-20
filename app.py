import json
import yaml
import pymysql
from flask import Flask, request, jsonify, make_response
app = Flask(__name__)


def db_connection():
    conn = None
    try:
        db_creds = yaml.load(open('creds.yaml'))
        conn = pymysql.connect(host=db_creds['RDS_host'],
                               user=db_creds['RDS_user'],
                               password=db_creds['RDS_pass'],
                               database=db_creds['mysql_db'],
                               #port=int(3306),
                               charset='utf8mb4',
                               cursorclass = pymysql.cursors.DictCursor
                               )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route('/')
def index():
    my_resp = make_response('Response!')
    my_resp.headers['Custom header'] = "Cheems"
    return my_resp
    
def get_redirect_if_exists(request):
    redirect = None

    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))

    return redirect

@app.route('/allblooddonors', methods = ['GET'])
def blood():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from blood")
    donors = [
        dict(Blood_Bank_Name = row['blood_bank_name'],
        Location = row['location'], Mobile_no = row['mobile_no'], Blood_Group = row['blood_group'])
        for row in cursor.fetchall()
    ]
    if donors is not None:
       return jsonify(donors) 

@app.route('/populateblooddonors', methods = ['POST'])
def populate():
    conn = db_connection()
    cursor = conn.cursor()    
    new_name = request.form['blood_bank_name']
    new_loc = request.form['location']
    new_no = request.form['mobile_no']
    new_group = request.form['blood_group']
    sql = '''INSERT INTO blood (blood_bank_name, location, mobile_no, blood_group) 
             VALUES (%s,%s,%s, %s)'''
    cursor = cursor.execute(sql,(new_name, new_loc, new_no, new_group))
    return "Entry Recorded successfully"


if __name__ == '__main__':
    app.run()
