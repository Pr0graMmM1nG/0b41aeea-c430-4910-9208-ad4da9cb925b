import Function as F
F.StartGames()

matrix=F.InitMatrix()
F.display_state_screen(matrix)

PlayerXValue=[]
PlayerOValue=[]
Player='X'
Count=9

while F.CountHods(PlayerXValue,PlayerOValue)<Count:
	if F.Wins(PlayerXValue):
		print ('Player X wins: ')
		break
	if F.Wins(PlayerOValue):
		print ('Player O wins ')
		break
		
	print('{0}>>>>'.format(F.CountHods(PlayerXValue,PlayerOValue)))
	print('Player {0} input value:'.format(Player))
	
	userInput = F.GetUserValue()
	#F.display_state_screen(matrix)
	
	if F.SameHodsExist(PlayerXValue,PlayerOValue,userInput):
		print('Value {0} exist in player {1}'.format(userInput, Player))
	else:
		#print('Value {0} no exist in {1}'.format(userInput, 'Players'))
		if Player=='X':
			print('add x value')
			PlayerXValue.append(userInput)
		else:
			print('add o value')
			PlayerOValue.append(userInput)
			
		F.ModifyMatrix(matrix,userInput,Player)
		F.display_state_screen(matrix)
		Player=F.NextPlayer(Player)
input("press enter to exit...")
