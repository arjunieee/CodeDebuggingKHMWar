for i in range(int(input())):				#explicit data type definition 
        word = input()
        word=word.upper()
        vowels = ['A','E','I','O','U']
        count = 0					#changed == to =
        for j in range(0,len(word)-1):			#function name changed to len and added : 
                if word[j] not in vowels:		#removed [] and added not
                        if j == 0:			#changed = to == 
                                count=count+1		#Increment operator doesn't exist 
                        elif word[j+1] not in vowels:	#removed [] and added not
                                break
                        else:
                                count=count+1		#increment operator doesn't exist
        print (count) 
