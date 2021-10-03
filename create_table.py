import pymysql
db_creds = yaml.load(open('creds.yaml'))
conn = pymysql.connect(host=db_creds['RDS_host'],
                       user=db_creds['RDS_user'],
                       password=db_creds['RDS_pass'],
                       database=db_creds['mysql_db'],
                       port=int(3306),
                       charset='utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor
                       )

cursor = conn.cursor()
sql_query = ''' CREATE TABLE blood (
    blood_bank_name text NOT NULL,
    location text NOT NULL,
    mobile_no text NOT NULL,
    blood_group text NOT NULL 
)'''

cursor.execute(sql_query)
conn.close()