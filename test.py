import time



def hello():

    
	time.sleep(2)
	print('Hello')
	
def hello1():
	time.sleep(2)
	print('Hello1')

def hello2():
	time.sleep(3)
	print('Hello2')


import pandas as pd 
 
def excel():
	df=pd.read_excel('test.xlsx')
	result=df.Values.values
	result=result.tolist()
	return result