
import mysql.connector
import pandas as pd

db_con = mysql.connector.connect(host='localhost',
                                 database='employee',
                                 user='root',
                                 password='123456789')

cursor = db_con.cursor()

#sql = "select * from employees where Salary=(select max(Salary) from employees);"  # these sql query prints highest salary and his details
sql="select * from employees"

cursor.execute(sql)

data = cursor.fetchall()
# print(data)
for i in data:
    # print(data)
    df = pd.DataFrame(data, columns=['person_id', 'first_name', 'last_name', 'Address', 'salary'])
print(df)
#print(type(df))

