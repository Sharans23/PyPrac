from functools import reduce
# filter function
nums=[1,2,3,4,5,5,6,7,8,9]

def is_even(n):
    if(n%2==0):
        return n

evens=list(filter(is_even,nums))

print(evens)

# or

# using lambda function
even=list(filter(lambda n:n%2==0,nums))
print(even)

# map function
doubles=list(map(lambda n:n*2,evens))
print(doubles)

# reduce function
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
