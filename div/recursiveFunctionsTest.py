def factorial(n):
  # factorial gets called over and over again, until n<=1.
  print(f"factorial() called with n = {n}")
  return_value = 1 if n <= 1 else n * factorial(n -1)
  # return value is then first 1, returning the 1 to the funciton
  # where n was 2, which will then return 2*1=2 to the function where
  # n was 3, which will then return 2*3=6 to the calling instance (this script)
  # all callers get the callees results and use it. So it goes all the way back
  # to the first calling funciton which then returns the final result.
  print(f"-> factorial({n}) returns {return_value}")
  return return_value

print('factorial(3) equals ',factorial(3))



def recTest(n):
    # in this example, recTest is called over and over again, till n>=5.
    # if so, the last called version returns 100 and thats it. The other called
    # instances from before die out.
    if n<5:
        print('calling recTest with n = ',n+1)
        recTest(n+1)
    else:
        print('returning 100 because n = ',n)
        return 100


recTest(1)


# traverse a nested list using recursion
namesTree = ["Adam", [ "Bob", [ "Chet", "Cat" ], "Barb", "Bert" ],"Alex", ["Bea","Bill" ], "Ann"]
    
# names is the current (flat) list. for each element in this list:
# call traverse again if the element is a list, otherwise print the element.
# count the non-list elements in the list and return it.
# Add the count from subcalls to get the final number of items.
def traverse(names):
    n=sum([type(i)!=list for i in names]) #names in this list
    for ele in names:
        if type(ele)==list: #sublist
            print('re-calling with list',ele)
            n+=traverse(ele)
        else:
            print(ele)
    return n

print(f'There are {traverse(namesTree)} names in the list')

#  even shorter, because the list comprehension
# corresponds to the else path!
def traverse1(ls):
    n=0
    for e in ls:
        if type(e)==list: n += traverse(e)
        else: n+=1
    return n
print(f'There are {traverse1(namesTree)} names in the list')

#  even shorter, with short if else
def traverse2(ls):
    n=0
    for e in ls: n += traverse(e) if type(e)==list else 1
    return n
print(f'There are {traverse2(namesTree)} names in the list')
