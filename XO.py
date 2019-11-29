import Function as F
row1=['1','1','1']
row2=['2','2','2']
row3=['3','3','3']	
matrix=F.getMatrix(row1,row2,row3)

F.display_state_screen(matrix)

userInput = F.GetUserValue()

Find=F.GetRowCol(userInput)

print(Find)
input("press enter to exit...")
