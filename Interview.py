cashbacks = []

def solution(balances, requests):
    for i in range(len(requests)):
        request=requests[i]
        components = request.split(" ")
        
        ## Invalid acccount number
        holder_id = int(components[2])-1
        timestamp = int(components[1])
    
            
        if holder_id not in range(len(balances)):
            return [-(i+1)]
           
        else:
            c1=[i for i in cashbacks if (int(i.split(" ")[0]) < timestamp) and (int(i.split(" ")[1]) == holder_id)] 
            for i in c1:
                balances[holder_id] = balances[holder_id] + int(i.split(" ")[2])
                position=cashbacks.index(i)
                cashbacks.pop(position)
            
                
            if components[0] == 'withdraw':
                if int(components[3]) > balances[holder_id]:
                    return [-(i+1)]
                else:
                    balances[holder_id] = balances[holder_id] - int(components[3])
                    cashbacks.append(str(timestamp+86400)+" "+str(holder_id)+" "+str(int(int(components[3]) * 0.02))) 
                
            if components[0] == 'deposit':
                balances[holder_id] = balances[holder_id] + int(components[3])
             
    return balances
                

    
balances=[1000,200]
requests = ["withdraw 100000 1 500","withdraw 200000 1 400","withdraw 200100 1 450","deposit 300000 2 100"]    

print(solution(balances,requests))