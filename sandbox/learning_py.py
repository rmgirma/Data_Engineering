
a= [1,2,3]
b= ['A','B','C']

for ai in a:
    for bj in b:
         print(ai,bj, end='')
    print(ai)
print("---------")

team = ['Robel', 'Sinidu', 'Nathan', 'Deena','Lina']
for me in team:
     for others in team:
        if me != others:
            print(me, others)
        else:
            print(me + " resting this week")
