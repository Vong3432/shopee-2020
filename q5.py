
output = 0 # total divisible

sequences = [
    [(1,1), (1,1)],
    [(1,1), (1,2)],
    [(1,1), (2,1)],
    [(1,2), (1,1)],
    [(1,2), (1,2)],
    [(1,2), (2,1)],
    [(2,1), (1,1)],
    [(2,1), (1,2)],
    [(2,1), (2,1)],
    [(2,1), (2,2)],
    [(2,1), (3,1)],
    [(3,1), (2,3)],
]

inputs = [
    [3,2,6],
    [0,3,2],
    [1,2,3],
    [2,5,1],
]

for input in inputs:

    Ai = input[0] # input 1, N
    Bi = input[1] # input 2, M
    Ci = input[2] # input 3, K
    k = Ci

    if((Ai >= 1 and Ai <= 5000) 
        and (Bi >= 1 and Bi <=  1000000000) 
        and (Ci >= 1 and Ci <= 2000)
        ):
        
        for x in sequences:           

            num1, num2 = x[0][0], x[0][1]                        
            # e.g n((1,1), (1,1))
            def n(i, j):       
                # something ...                                           
                
                # j2 = sequences[1][1]                                
                # return ((Ai * j2[0]) * j[1]) +  Bi
                
                return Ai * j[1] +  Bi

            def test():
                val = n(x[0], x[1])

                if(val % k == 0):
                    global output
                    output = output + 1                                                                                    

            test()
        
print(output)