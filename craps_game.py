import random

def Roll():
	d1 = random.randint (1,6)
	d2 = random.randint (1,6)
	return int (d1 + d2)
	
def ComeOutRoll():
	roll = Roll()
	print('Come-Out Roll: ' + str(roll))
	
	if roll in [7, 11]:
		print('A Natural, You win!')
	elif roll in [2,3,12]:
		print('Craps! You lose!')
	elif roll in [4,5,6,8,9,10]:
		print('Point: '+ str(roll))
		while True:
			done = RollDice(roll)
			if done:
				break
	
	
def	RollDice(point):
	roll = Roll()
	print(' Roll: ' + str(roll))
	
	if not roll in [7, point]:
		print('Roll again!')
	elif roll in [point]:
		print('Point-Match')
		return True
	elif roll in [7]:		
		print('Seven-Out!\nYou lose!\nGame Over!')
		return True
	