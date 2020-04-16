'''
The task assigned was to simulate the operation and functionality of an elevator in an N story building. I have completed the task with the following assumptions:
 
1. The elevator boards only one person from each floor.
2. There is no restriction on lift capacity.

Flow of execution:
	1. The user is prompted to enter the number of floors.

				Enter the number of floors of the building 10

	2. The user has to decide whether he/she wants to travel up or down.

		Direction
			1 Upwards
			0 Downwards

			1

	3. The elevator requires the number of such people who are travelling in the same direction.
	
			
			Enter the number of people accessing the lift: 5


	4. The individual information about each user accessing the lift is required.i.e the floor the individuals are at . 

				which floor are the users at 1
				which floor are the users at 3
				which floor are the users at 5
				which floor are the users at 2
				which floor are the users at 6


		


	5. After the user steps in . He/she is required to input the floor they would like to get down at.
		
		The lift is empty.
		picked up 1  person from 1  floor
		1  people  is/are in the lift currently
		where do you want to go? 3


	6. The information of the elevator is displayed on each floor 






sample test case : 

10
 
 1

	5
 
	3
	2
 	1
 	5
 	7

 	3
 	4
 	4
 	9
 	9


'''


def goUp(liftPos,maxFLoor,waitLift,qLift,):
	dest=[]
	
	while liftPos<=maxFLoor:
		
	

		if liftPos in waitLift:
			x=len(qLift)
			print('picked up',len(qLift)+1,' person from',liftPos,' floor')
			qLift.append(waitLift.pop(0))
			print(len(qLift),' people  is/are in the lift currently')
			destination=int(input("where do you want to go? "))
			dest.append(destination)
			maxFLoor=max(dest)
			
		if liftPos in dest:
			
			if dest.count(liftPos)>1:
				
				while dest.count(liftPos)>=1:
					na=dest.index(liftPos)
			
					del dest[na]
					del qLift[na]
					na=na+1
			else:
				na=dest.index(liftPos)
				
				del dest[na]
				del qLift[na]
		display(liftPos,1)
		if len(qLift)>0:
			print(len(qLift),'members are in the lift.')
		else:
			print('The lift is empty.')	
		liftPos+=1	

def goDown(lift_floor,qLift,downLift,grndFloor):
	down_dest=[]
	while lift_floor>=0:
		

		if lift_floor in downLift:

			x=len(qLift)
			print('picked up ',len(qLift)+1,'person from',lift_floor,' floor')
			qLift.append(downLift.pop(0))
			print(len(qLift),' people  is/are in the lift currently')


			#print(qLift,'is in the lift')
			destination=int(input("where do you want to go? "))
		
			down_dest.append(destination)
			grndFloor=max(down_dest)
				
		if lift_floor in down_dest:
			
			if down_dest.count(lift_floor)>1:
			
				while down_dest.count(lift_floor)>=1:
					na=down_dest.index(lift_floor)
				
					del down_dest[na]
					del qLift[na]
					na=na+1
			else:
				na=down_dest.index(lift_floor)
				
				del down_dest[na]
				del qLift[na]
					
			
			if len(waitLift_unbounded)>0 and liftPos in dest:
				qLift.append(waitLift_unbounded.pop(0))
				destination=int(input("where do you want to go? "))
				dest.append(destination)		
				
			elif len(waitLift_unbounded)>0 and liftPos not in dest:
				while liftPos>waitLift_unbounded[0]:
					display(liftPos,0)
					liftPos-=1
					if liftPos==waitLift_unbounded[0]:
						display(liftPos,0)
				destination=int(input("where do you want to go? "))
				dest.append(destination)
				
		
		display(lift_floor,0)
		if len(qLift)>0:
			print(len(qLift),'members are in the lift.')
		else:
			print('The lift is empty.')		
		lift_floor-=1

def display(n,l):
	if l==0:
		l="down"
	elif l==1:
		l="up"	
	print(" ")	
	print(" ")
	print("The lift is at floor ",n,"with going",l,'direction')
	print("  ")
	print(" ")

maxFLoor1=int(input("Enter the number of floors of the building "))
waitLift1=list()
waitLift_unbounded=list()
print('Direction')
print('1 Upwards')
print('0 Downwards')

direction=int(input())
if direction==1:
	n=int(input("Enter the number of people accessing the lift: "))
	for i in range(0,n):
		temp=int(input("which floor are the users at "))
		#waitLift_unbounded.append(temp)
		waitLift1.append(temp)
	liftPos1=0
	# print(len)
	waitLift1.sort()
	qLift1=[]
	

	
	goUp(liftPos1,maxFLoor1,waitLift1,qLift1)
else:
	downLift1=list()

	a=int(input("Enter the number of accessing the lift: "))
	for i in range(0,a):
		temp=int(input("which floor are the users at "))
		#waitLift_unbounded.append(temp)
		downLift1.append(temp)
	
	# print(len)
	# print(downLift)
	downLift1.sort(reverse=True)
	



	grndFloor1=0
	qLift1=[]
	goDown(maxFLoor1,qLift1,downLift1,grndFloor1)

