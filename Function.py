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
	