def hexagon_pattern(rows, cols):
    for row in range(rows):
        for col in range(cols):
            print("  ___  ", end=" ")
        print()
        
        
        for col in range(cols):
            if col < 4:
                if col == 0:
                    print(" /   \___/", end=" ")
                else:
                    print("  \___/", end=" ")
            else:
                print("  \ ", end=" ")
                    
        print()
    
        
        
        
        for col in range(cols):
            if col % 2 == 0 :
                print(" \___/ ", end=" ")
            else:
                print(" \___/ ", end=" ")
            
        print()
        
       

rows = 3
cols = 5
hexagon_pattern(rows, cols)
