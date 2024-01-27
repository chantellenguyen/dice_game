import random
#lives=<3<3<3
# 1. listname.append()
# 2. random.choice(listname)
# 3. listname[0] + .....
# 4. sum(listname)

list=[1,2,3,4,5,6]




userdice=[]
computerdice=[]

userdice.append(random.choice(list))
userdice.append(random.choice(list))
userdice.append(random.choice(list))

computerdice.append(random.choice(list))
computerdice.append(random.choice(list))
computerdice.append(random.choice(list))

va=sum(userdice)
var=sum(computerdice)

if(va==var):
  print("tie!!")
elif(va>var):
  print("U WIN!!YAY!")
else:
  print("u lose awww")
