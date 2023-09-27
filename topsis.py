import math
q = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ]
wt=[0.3,0.5,0.2]

def normalization(x):
    qDash=[]
    den = []
    for i in range(len(x)):
        sq = 0
        for j in range(len(x)):
            sq = sq+x[j][i]**2
        den.append(math.sqrt(sq))
        
    for k in range(len(x)):
        temp = []
        div=0
        for l in range(len(x)):
            div = x[k][l]/den[l]
            temp.append(div)
        qDash.append(temp)
        
    return(qDash)

def weighted(y,weight):
    v = []
    for i in range(len(y)):
        temp = []
        for j in range(len(y)):
            temp.append(weight[j]*y[i][j])
        v.append(temp)
    return(v)

def iPlus(v):
    pos=[]
    for i in range(len(v)):
        max = 0
        for j in range(len(v)):
            if v[j][i]>max:
                max = v[j][i]
        pos.append(max)
    return pos

def iMinus(v):
    neg = []
    for i in range(len(v)):
        min = 1000
        for j in range(len(v)):
            if v[j][i]<min:
                min = v[j][i]
        neg.append(min)
    return neg
    
def posCloseness(v,pos):
    
    res = []
    for i in range(len(v)):
        clPlus = 0
        for j in range(len(v)):
            temp = pos[j]-v[i][j]
            clPlus = clPlus+ temp**2
        clPlus = math.sqrt(clPlus)
        res.append(clPlus)
    return res

def negCloseness(v,neg):
    res = []
    for i in range(len(v)):
        clMinus = 0
        for j in range(len(v)):
            temp = neg[j]-v[i][j]
            clMinus = clMinus+ temp**2
        clMinus = math.sqrt(clMinus)
        res.append(clMinus)
    return res

def relCloseness(clPlus,clMinus):
    res = []
    for i in range(len(clPlus)):
        temp = clPlus[i]+clMinus[i]
        temp = clMinus[i]/temp
        res.append(temp)
    return res

print(q)
print()
print()

normalizedMatrix = normalization(q)
print(normalizedMatrix)
print()
print()
weightedMatrix = weighted(normalizedMatrix,wt)
print(weightedMatrix)
print()
print()
positiveIdeal = iPlus(weightedMatrix)
print(positiveIdeal)
print()
print()
negativeIdeal = iMinus(weightedMatrix)
print(negativeIdeal)
print()
print()
positiveCloseness = posCloseness(weightedMatrix,positiveIdeal)
print(positiveCloseness)
print()
print()
negativeCloseness = negCloseness(weightedMatrix, negativeIdeal)
print(negativeCloseness)
print()
print()
relativeCloseness = relCloseness(positiveIdeal,negativeIdeal)
print(relativeCloseness)