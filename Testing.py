"""def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  l=[]
  for i in range(N):
    if C[i]=='B':
      l.append('A')
    else:
      l.append('B')
  return "".join(l)


print(getWrongAnswers(3,'BBA'))"""

inputDict = {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}

def return_smallest_key(inputDict, n):
  # Write your code here
  l=[]
  for k,v in inputDict.items():
    l.append([v,k])
  l.sort()
  if n>len(l):
    return None
  else:
    return l[n-1][1]

print(return_smallest_key(inputDict,5))