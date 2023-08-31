#making functions which take input and store data in lists

def cricket():
	cric_roll = []
	cric_num = int(input("Enter the number of students playing cricket: "))
	for i in range (cric_num):
		x = int(input("Please enter roll no. of cricket player: "))
		cric_roll.append(x)
	return cric_roll	
	
def football():
	foot_roll = []
	foot_num = int(input("Enter the number of students playing football: "))
	for i in range (foot_num):
		x = int(input("Please enter roll no. of football player: "))
		foot_roll.append(x)
	return foot_roll	
	
def badminton():
	badm_roll = []
	badm_num = int(input("Enter the number of students playing badminton: "))
	for i in range (badm_num):
		x = int(input("Please enter roll no. of badminton player: "))
		badm_roll.append(x)
	return badm_roll	

# storing lists of roll numbers of players of 3 games.
lst1 = cricket()
lst2 = badminton()
lst3 = football()

# creating function for union list (all students who play a game).
def union(lst1, lst2, lst3):
	i = 0
	union_list = []
	temp = []
	
	temp = lst1 + lst2 + lst3 
	for i in temp:
		if i not in union_list:
			union_list.append(i)
		else:
			continue
	return union


#below code is long and the function can be performed in few lines as done in the code above.

'''union_list = []
	i = 0
	for i in lst1:
		if i in union_list:
			continue
		else:
			union_list.append(i)
	j = 0
	for j in lst2:
		if j in union_list:
			continue
		else:
			union_list.append(j)
	k = 0
	for k in lst3:
		if k in union_list:
			continue
		else:
			union_list.append(k)
	return union_list'''

# function for finding the students who play all the games.
def anbnc(lst1, lst2, lst3):
	inter_abc = []
	inter = []
	i = 0
	for i in lst1:
		if i in lst2 and lst3:
			inter_abc.append(i)
		else:
			continue
	j = 0 
	for j in lst2:
		if j in lst1 and lst3:
			inter_abc.append(j)
		else:
			continue
	k = 0
	for k in lst3:
		if k in lst1 and lst2:
			inter_abc.append(k)
		else:
			continue
	l = 0 			
	for l in inter_abc:
		if l not in inter:
			inter.append(l)
		else:
			continue
			
	return inter
	
	
intersection = anbnc(lst1, lst2, lst3)
print("The intersection of all students: ", intersection)

unionres = union(lst1, lst2 ,lst3 )
print("The Union set of all students: ",unionres)

















































