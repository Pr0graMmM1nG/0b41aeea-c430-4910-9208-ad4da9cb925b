import Function as F
row1=['1','1','1']
row2=['2','2','2']
row3=['3','3','3']	


matrix = [['#','a','b','c'],F.merge_row(['a'],row1),F.merge_row(['b'],row2),F.merge_row(['c'],row3)]
F.display_state_screen(matrix)
print(row1)
print(row2)
print(row3)
input("press enter to exit...")
