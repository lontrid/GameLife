import random
import time  
import os 
import sys
ocean = []
ocean.append(['N','N','N','N','N','N','N','N','N','N',
'N','N','N','N','N','N','N','N','N','N',
'N','N','N','N','N','N','N','N','N','N'])
for number in range(28):
    row = []
    row.append('N')
    for number in range(28):
        row.append(random.choice('FSRN'))
	# F - Fish
	# S - Shrimp
	# R - Rock
	# N - Nothing
    row.append('N')
    ocean.append(row)
ocean.append(['N','N','N','N','N','N','N','N','N','N',
'N','N','N','N','N','N','N','N','N','N',
'N','N','N','N','N','N','N','N','N','N'])
while True:
    f=0
    s=0
    for q in range(30):
        for w in range(30):
            print(ocean[q][w].center(2),end='')
        print()
    for i in range(1,29):
        for j in range(1,29):
            if ocean[i][j] == 'N':
                neighbors = 0
                if(ocean[i-1][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i-1][j]=='F'):
                    neighbors = neighbors+1
                if(ocean[i-1][j+1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j+1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i][j+1]=='F'):
                    neighbors = neighbors+1
                if(neighbors==3):
                    ocean[i][j]='F'
            if ocean[i][j] == 'N':
                neighbors = 0
                if(ocean[i-1][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i-1][j]=='S'):
                    neighbors = neighbors+1
                if(ocean[i-1][j+1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j+1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i][j+1]=='S'):
                    neighbors = neighbors+1
                if(neighbors==3):
                    ocean[i][j]='S'
            if ocean[i][j] == 'F':
                neighbors = 0
                f=f+1
                if(ocean[i-1][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i-1][j]=='F'):
                    neighbors = neighbors+1
                if(ocean[i-1][j+1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j]=='F'):
                    neighbors = neighbors+1
                if(ocean[i+1][j+1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i][j-1]=='F'):
                    neighbors = neighbors+1
                if(ocean[i][j+1]=='F'):
                    neighbors = neighbors+1
                if(neighbors>=4):
                    ocean[i][j]='N'
                if(neighbors<2):
                    ocean[i][j]='N'
            if ocean[i][j] == 'S':
                neighbors = 0
                s=s+1
                if(ocean[i-1][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i-1][j]=='S'):
                    neighbors = neighbors+1
                if(ocean[i-1][j+1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j]=='S'):
                    neighbors = neighbors+1
                if(ocean[i+1][j+1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i][j-1]=='S'):
                    neighbors = neighbors+1
                if(ocean[i][j+1]=='S'):
                    neighbors = neighbors+1
                if(neighbors>=4):
                    ocean[i][j]='N'
                if(neighbors<2):
                    ocean[i][j]='N'
    print(str(f)+" fish")
    print(str(s)+" shrimp")
    time.sleep(2)
    os.system('clear')