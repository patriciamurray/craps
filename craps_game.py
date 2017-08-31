import random

class Craps(object)
	CRAPS_KEY = "craps" 
 	DONE_KEY = "done" 
 	POINT_KEY = "point" 
 	BET_KEY = "bet" 
 	SURRENDER_KEY = "surrender" 

	
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

def	play_pass_line(self, bet):
	if self.game.is_point_on():
		return False
		
	elif self.pass_line_bet = bet:
		return True
		
def play_pass_line_odds(self, bet):	
	if self.game.is_point_on() and self.pass_line_bet != 0:
		self.pass_line_odds = bet
		return True
	elif 
		return False
	