import random

i=open('participants.txt','r')
s=i.readline()
participants=list(map(str,s.split()))
num_winners=int(input())
if num_winners>=len(participants):
    print('Too many partipants to choose. Press Enter to try again')
else:
    winners=random.sample(participants,num_winners)
    print(winners)
