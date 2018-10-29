import sys
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score 
        
    def __repr__(self):
        print "why this function?"
        
        
    def comparator(a, b):      
        if a.score < b.score:
            return 1
        
        if b.score < a.score:
            return -1
        
        if b.score == a.score:      
            if cmp(a.name, b.name) == 1:
                return 1
        
            if cmp(a.name, b.name) == -1:
                return -1
        
            if cmp(a.name, b.name) == 0:
                return 0
        
    
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
