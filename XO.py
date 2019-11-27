def show_list(list):
	string=''
	for item in list:
		string+=item+'   '
	print(string,end='')
def display_state_screen(state_screen):
	print('Result:')
	for i in state_screen:
		show_list(i)
		print('\n')
initial_state_screen = [['#','a','b','c'],['a','1','1','1'],['b','2','2','2'],['c','3','3','3']]
display_state_screen(initial_state_screen)

input("press enter to exit...")