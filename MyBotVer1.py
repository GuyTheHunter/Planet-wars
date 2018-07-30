import math

def do_turn(pw):
    if len(pw.my_fleets()) >= 1:
        return
    if len(pw.my_planets()) == 0:
        return
	if len(pw.neutral_planets()) == 0 and len(pw.enemy_planets()) == 0:
		return
	
	#s = Source(pw.my_planets())
    num_ships = Source(pw.my_planets()).num_ships() / 2
	
    pw.issue_order(Source(pw.my_planets()), Close(Source(pw.my_planets()), list(set(pw.neutral_planets() + pw.enemy_planets()))), num_ships)

def Distance(source, dest):
	x = math.pow((source.x() - dest.x()), 2)
	y = math.pow((source.y() - dest.y()), 2)
	
	return math.sqrt(x + y)	
	
def Close(source, dests):
	minIndex = 0
	Index = 0
	for dest in dests:
		if Distance(source, dest) < Distance(source, dests[minIndex]):
			minIndex = Index
		Index = Index + 1
		
	return dests[minIndex]
	
def Source(sources):
	maxIndex = 0
	Index = 0
	for s in sources:
		if s.num_ships() > sources[maxIndex].num_ships():
			maxIndex = Index
		Index = Index + 1
		
	return sources[maxIndex]
