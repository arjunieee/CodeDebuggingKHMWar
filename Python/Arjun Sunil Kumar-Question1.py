#removed Input from first line
n = int(input("Enter number of elements : "))
Input = list(map(int, input().split()))#changed the way values were inputted 
if(Input[0]<0):
    	prev =1
else:
    	prev=-1
ans=-1#initialised ans with -1
for elem in Input: 
	if (elem==0):#changed = to == and added parantheses 		
		sign = 1
	else: 
		sign = elem / abs(elem) 

	if sign == -prev: 		
		ans = ans + 1
		prev = sign  
print(ans)#changed the variable to printed to ans

