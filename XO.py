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
	
	
row1=['1','1','1']
row2=['2','2','2']
row3=['3','3','3']	
	
matrix = [['#','a','b','c'],merge_row(['a'],row1),merge_row(['b'],row2),merge_row(['c'],row3)]
display_state_screen(matrix)
print(row1)
print(row2)
print(row3)

input("press enter to exit...")