#python3 guess number
ans = 29
fla = 0
for guesscount in range(0,3):
	a = int(input ("Please input a number(1~30) : "))
	if a == ans :
		print("You got it!")
		fla = 1
		break
	else : 
		print("Wrong!")
if fla == 1 :
	print("Finished.")
else :
	print("Game Over.")