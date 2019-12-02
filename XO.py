import Function as F
F.StartGames()

matrix=F.InitMatrix()
F.display_state_screen(matrix)

PlayerXValue=[]
PlayerOValue=[]
Player='X'
Count=9

while F.CountHods(PlayerXValue,PlayerOValue)<Count:
			
	print('{0}>>>>'.format(F.CountHods(PlayerXValue,PlayerOValue)))
	print('Player {0} input value:'.format(Player))
	
	userInput = F.GetUserValue()

	if F.SameHodsExist(PlayerXValue,PlayerOValue,userInput):
		print('Value exist {0}'.format(userInput))
	else:
		if Player=='X':
			print('add x value')
			PlayerXValue.append(userInput)
		else:
			print('add o value')
			PlayerOValue.append(userInput)
			
		F.ModifyMatrix(matrix,userInput,Player)
		F.display_state_screen(matrix)

		Player=F.NextPlayer(Player)
		
	if F.Wins(PlayerXValue):
		print ('Player X wins: ')
		break
	if F.Wins(PlayerOValue):
		print ('Player O wins ')
		break

input("press enter to exit...")
