
#sort algorithm

def sort_list(input_list):
    for i in range(len(input_list)-1):
        position=i
        value=input_list[i]
        for j in range(i+1,len(input_list)):
            if input_list[j]<value:
                input_list[position]=input_list[j]
                input_list[j]=value
                value=input_list[position]
    return input_list
    
print(sort_list([19,4,3,6,9,19,5,1]))
