with open ('data.txt', 'r') as infile:
    #make list of 'line' strings
    lines=infile.readlines()
    
count=0 
for line in lines:
    #split string into list 
    obj=line.split()
    
    #get a list of acceptable character frequencies in string, assign obj[0]
    start_end_int=list(map(int,obj[0].split('-')))
    obj[0]=list(range(start_end_int[0],start_end_int[1]+1))
    
    #format string charcter for searching
    obj[1]=obj[1].replace(':','')
    
    #see if letter frequency is acceptable
    if obj[2].count(obj[1]) in obj[0]:
        count+=1


print(count)
