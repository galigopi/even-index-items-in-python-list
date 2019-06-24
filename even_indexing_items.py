a=["gopi","krishna","love","python"]
b_even=[]
c_odd=[]
index=0
for item in a:
    if index % 2 != 0:
        b_even.append(item)
    else:
        c_odd.append(item)
    index+=1
print ("even index words",b_even)
print ("odd index words",c_odd)
