

def show_list(list):
	string=''
	for item in list:
		string+=item+'   '
	print(string,end='')

def display_state_screen(matrix_state):
	print('Result:')
	for i in matrix_state:
		show_list(i)
		print('\n')

def merge_row(list1,list2):
	list1.extend(list2)
	return list1

def getMatrix(list1,list2,list3):
	matrix = [['#','a','b','c'],merge_row(['a'],list1),merge_row(['b'],list2),merge_row(['c'],list3)]
	return matrix

def GetRowCol(UserValue):
	temp = str(UserValue)
	row=0
	col=0
	if temp[0]=='a':
		row=1
	elif temp[0]=='b':
		row=2
	elif temp[0]=='c':
		row=3
	if temp[1]=='a':
		col=1
	elif temp[1]=='b':
		col=2
	elif temp[1]=='c':
		col=3
	RowCol=[row,col]
	return 	RowCol	

def InputUser():
	GetUserString=input("Please select Row and Col {0}".format('ex.(ab = row#1 and col#2):'))[:2]
	return GetUserString
def SelectPattern (userValue):
	import re
	pattern=re.search('[a-c]{2}',userValue)
	return pattern

def GetUserValue():
	userValue = InputUser()
	pattern = SelectPattern(userValue)
	while pattern==None:
		print('Wrong input data: {0} pattern is: {1}'.format(userValue,pattern))
		userValue = InputUser()
		pattern = SelectPattern(userValue)
	else:
		print('User select: {0}'.format(userValue))
	return userValue