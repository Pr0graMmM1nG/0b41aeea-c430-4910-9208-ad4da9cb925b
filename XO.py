import Function as F
F.StartGames()

matrix=F.InitMatrix()
F.display_state_screen(matrix)

PlayerXValue=[]
PlayerOValue=[]
Player='X'
Count=9

while F.Hods(PlayerXValue,PlayerOValue)<Count:
	print('Make: {0} pass'.format(F.CountHods(PlayerXValue,PlayerOValue)))
	print('Player {0}:'.format(Player))
	
	userInput = F.GetUserValue()
	##input logika in caz ca deja asa hod sa facut
	if F.ifExist_UserValue(PlayerXValue,userInput):
		print('Value exist please select another value')
	else:
		print('No exist:Append value {0} in depositValue'.format(userInput))
		if Player=='X':
			PlayerXValue.append(userInput)
			print('Show value of Player{1}Value: {0}'.format(PlayerXValue,Player))
		else:
			PlayerOValue.append(userInput)
			print('Show value of Player{1}Value: {0}'.format(PlayerOValue,Player))
	matrix=F.ModifyMatrix(matrix,userInput,Player)
	F.display_state_screen(matrix)
	Player=F.NextPlayer(Player)
	
	
	

input("press enter to exit...")
