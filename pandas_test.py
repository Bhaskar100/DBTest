import  pandas as pd
import cx_Oracle
import logging
import matplotlib.pyplot as plt


# Inserting a record into a table in Oracle database
try:
	con = cx_Oracle.connect('DWH1/100100@localhost:1521/xe')
	cursor = con.cursor()

	#con.autocommit = True
	# Inserting a record into table employee
	sql_str = 'select * from human'
	pp = pd.read_sql(sql_str,con)
	print('dataframe')
	print(pp)
	print('--------------------')
	print(pp.iloc[[1], [0]])
	pp.iloc[[1], [0]] = 'Johnson'
	print(pp.iloc[[1], [0]])
	pp.at[4,'STATE'] = 'Andhra'
	print()
	print(pp)




	"""
	print('--------------------')
	print(pp.iloc[1])
	print()
	print('--------------------')
	print(pp.iloc[[1],[0]])
	print()
	
	print(pp.dtypes)

	print('--------------------')
	print(pp.tail())

	print('--------------------')
	print(pp.head())

	pp.to_csv('human.csv')
	
	age = pp['AGE'].astype(int)
	print(pp.dtypes)

	high = list(age.values.tolist())
	mm = list(filter(lambda x : x > 25,high))
	print()
	print()
	print(mm)
	print(pp[pp.FNAME ==  'Harry'])
	print('------------------------------- Tommorow ------------------------')
	pts = pp['PETS'].astype(int)
	pr = pp['PETS'].astype(int)
	pts = list(pts.values.tolist())
	ps = list(map(lambda x: x * x , pts))
	pp['PETS'] = pr.apply(lambda x: x + 1)
	pp['STATE'] = 'Andhra'
	print()
	print("=============")
	print(pp)
	df = pd.read_csv('human.csv')
	print(df)
	
	print('================================ Matplotlib =======================================')
	#plt.pie(pp["AGE"], labels=pp["FNAME"])
	#plt.show()

	#plotting a line graph
	print("Line graph: ")
	plt.plot(pp["FNAME"], pp["AGE"])
	plt.show()


	# plotting a scatter plot
	print("Scatter Plot:  ")
	plt.scatter(pp["FNAME"], pp["PETS"])
	plt.show()
	"""




except Exception as e:
	logging.error("error message" , e)
