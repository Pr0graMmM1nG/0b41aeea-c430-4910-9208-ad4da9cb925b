def InitMatrix():
	row1=['*','*','*']
	row2=['*','*','*']
	row3=['*','*','*']	
	matrix=getMatrix(row1,row2,row3)
	return matrix
	
def getMatrix(list1,list2,list3):
	matrix = [['#','a','b','c'],merge_row(['a'],list1),merge_row(['b'],list2),merge_row(['c'],list3)]
	return matrix
	
def show_list(list):
	string=''
	for item in list:
		string+=item+'   '
	print(string,end='')

def display_state_screen(matrix_state):
	print('_______________')
	for i in matrix_state:
		show_list(i)
		print('\n')

def merge_row(list1,list2):
	list1.extend(list2)
	return list1

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
	GetUserString=input("ex.(ab = row#1 and col#2):")[:2]
	return GetUserString
	
def SelectPattern (userValue):
	import re
	pattern=re.search('[a-c]{2}',userValue)
	return pattern

def GetUserValue():
	userValue = InputUser()
	pattern = SelectPattern(userValue)
	while pattern==None:
		print('Error input: {0}, Please type again:'.format(userValue))
		userValue = InputUser()
		pattern = SelectPattern(userValue)
	else:
		print('Player selected: {0}'.format(userValue))
	return userValue
	
def ModifyMatrix (Matrix , UserValue, XO):
	RowAndCol=GetRowCol(UserValue)
	Matrix[RowAndCol[0]][RowAndCol[1]]=XO
	return Matrix

def ifExist_UserValue(AllValue, CurrentValue):
	countValue=0
	for item in AllValue:
		if item==CurrentValue:
			countValue+=1
	if countValue==0:
		return False
	else:
		return True
def StartGames():
	print('Begin game: Loading...')
	
def CountHods(PlayerX,PlayerO):
	x=len(PlayerX)
	y=len(PlayerO)
	return x+y
	
def NextPlayer(Player):
	if Player=='X':
		Player='O'
	else:
		Player='X'
	return Player

def Wins(PlayerHods):
	PlayerCase= set(PlayerHods)
	a=['aa','ab','ac']
	b=['ba','bb','bc']
	c=['ca','cb','cc']
	d=['aa','ba','ca']
	e=['ba','bb','bc']
	f=['ca','cb','cc']
	g=['aa','bb','cc']
	h=['ac','bb','ca']
	WinConditionArray= [a,b,c,d,e,f,g,h]
	for Wincase in WinConditionArray:
		item =  set(Wincase)
		if len(PlayerCase & item)==3:
			return True

def SameHodsExist (PlayerXhods,PlayerOhods,currentInput):
	flag = 0
	PlayerXhods.extend(PlayerOhods)
	flag=PlayerXhods.count(currentInput)
	if any(check in PlayerXhods for check in PlayerOhods) or len(PlayerXhods)!=len(set(PlayerXhods)) or len(PlayerOhods)!=len(set(PlayerOhods)):
		flag+=1	
	if flag>0:
		return True
	else:
		return False

		