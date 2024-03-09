for _ in range(4):
    x1,y1,a1,b1,x2,y2,a2,b2 = map(int, input().split())
    result = 'a'
    if x1>a2 or x2>a1 or y1>b2 or y2>b1:
        result = 'd'
    
    elif x1 == a2:
        if y1 == b2 or y2 == b1:
            result = 'c' 
        else:
            'b'

    elif x2 == a1:
        if y1 == b2 or y2 == b1:
            result = 'c' 
        else:
            'b'  
               
    elif y1 == b2:
        if x1 == a2 or x2 == a1:
            result = 'c' 
        else:
            'b'
        
    elif y2 == b1:
        if x1 == a2 or x2 == a1:
            result = 'c' 
        else:
            'b'
            
    print(result)