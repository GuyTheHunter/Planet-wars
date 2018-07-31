import math

def do_turn(pw):
	if len(pw.my_planets()) == 0:
		return
	if len(pw.neutral_planets()) == 0 and len(pw.enemy_planets()) == 0:
		return
	
	mainFunc(pw)
	
def mainFunc(pw):
	sources = pw.my_planets()
	enemies = list(set(pw.neutral_planets() + pw.enemy_planets()))
	
	enemy = GetEnemy(enemies)
	source = GetSource(sources, enemy, pw.enemy_planets())
	num_ships = GetShips(source, enemy)
	
	pw.issue_order(source, enemy, num_ships)
	
def Distance(source, dest):
	x = math.pow((source.x() - dest.x()), 2)
	y = math.pow((source.y() - dest.y()), 2)
	
	return math.sqrt(x + y)	
	
def GetSource(sources, enemy, enemies):
	scores = []
	score = 0
	
	for source in sources:
		if source.num_ships() >= enemy.num_ships():
			score = score + 1
		if Distance(source, enemy) < 275 and Distance(source, enemy) <= CloseDistance(enemies, enemy):
			score = score + 1
		scores.append(score)
		score = 0	
		
	return sources[scores.index(max(scores))]
	
def GetEnemy(enemies):
	scores = []
	score = 0
	
	for enemy in enemies:
		if enemy.owner() == 0:
			score = score + 1
		if enemy.num_ships() < 150:
			score = score + 1
		if enemy.growth_rate() >= 3:
			score = score + 1
		scores.append(score)
		score = 0
	return enemies[scores.index(max(scores))]
	
def GetShips(source, dest):
	if source.num_ships() >= dest.num_ships() + 100:
		return dest.num_ships() + 48
	return source.num_ships() / 2
	
def CloseDistance(enemies, dest):
	minIndex = 0
	Index = 0
	
	for enemy in enemies:
		if Distance(enemy, dest) < Distance(enemies[minIndex], dest):
			minIndex = Index
		index = Index + 1
	return Distance(enemies[minIndex], dest)
