# importing module
import cx_Oracle
import logging

# Inserting a record into a table in Oracle database
try:
	con = cx_Oracle.connect('DWH1/100100@localhost:1521/xe')
	cursor = con.cursor()

	#con.autocommit = True
	# Inserting a record into table employee
	cursor.execute('select * from employee100')
	rows = cursor.fetchall()
	logging.info('info message')
	logging.warning('Warning message')
	logging.critical('Critical message')
	for row in rows:
		print(row)

	# commit() to make changes reflect in the database
	con.commit()
	print('Record inserted successfully')

except cx_Oracle.DatabaseError as e:
	logging.error("error message" , e)
	print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
"""
1. Critical
2. Error
3. Warning
4. Info
5. Debug


"""