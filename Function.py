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

def GetUserValue():
	userInput= input('Run Player X: ')
	while len(userInput)!=2:
		print('Wrong Value: Please enter valid value.')
		userInput= input('Run Player X: ')
	else:
		print('User set: {0}'.format(userInput))
	