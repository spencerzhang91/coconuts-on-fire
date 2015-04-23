def safe(pawns):
    match_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    coords = []
    safe_pawn = 0
    for pawn in pawns:        
        coords.append((match_dict[pawn[0]],int(pawn[1])))
    for c in coords:
        guard_c1 = (c[0]-1, c[1]-1)
        guard_c2 = (c[0]+1, c[1]-1)
        if (guard_c1 in coords) or (guard_c2 in coords):
            safe_pawn += 1
    return safe_pawn
            
    
test = safe({'a1','b2','c2','c3','d2','d1'})
print(test)
