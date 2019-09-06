import datetime
x=datetime.datetime.now()
for i in range(100000):
    print(i**2)
y=datetime.datetime.now()
z=y-x
print("result= ",z.total_seconds(),"seconds")   
