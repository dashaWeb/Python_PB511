

while True:
    choise = int(input(''' Enter a shape variant:
            [1] - а   [2] - б  [3] - в   [4] - г  [5] - д 
                                              
            [6] - е   [7] - ж  [8] - з  [9] - и  [10] - к
            
                       [0] - вихід
                                               
    '''))

    if choise == 0:
        break

    line = 7


    match choise:
        case 2:
            for j in range(1, line + 1):            
                for i in range(1 , j + 1):
                    print("*",end=" ")
                print()
        case 1:
            q = 0
            for j in range(line , 0 , -1):
                print(' ' * q , end=' ')
                q += 2
                for i in range(1 , j + 1):
                    print('*',end=" ")
                print() 

        case 9:
            for j in range(line, 0, -1 ):            
                for i in range( 1, j + 1 ):
                    print( '*' , end=" ")
                print() 

        case 10:
            q = line*2 - 2  
            for j in range(1, line +1):
                print(' ' * q , end='')
                q -= 2            
                for i in range(1, j + 1 ):
                    print( '*' , end=" ")
                print()
        case 7:
            for j in range(1, line + 1):            
                if j < (line / 2) + 1 :
                    for i in range(1 , j + 1):
                        print("*",end=" ")
                    print()
            line = line // 2                   
            for j in range(line , 0, -1 ):                              
                for i in range( 1, j + 1 ):
                    print( '*' , end=" ")
                print()

        case 8:
            q = line*2 - 2  
            for j in range(1, line +1):
                if j < (line / 2) + 1 :
                    print(' ' * q , end='')
                    q -= 2            
                    for i in range(1, j + 1 ):
                        print( '*' , end=" ")
                    print()                  
            line = line // 2 
            q = line * 2 + 1
            for j in range(line , 0 , -1):
                print(' ' * q , end=' ')
                q += 2
                for i in range(1 , j + 1):
                    print('*',end=" ")
                print()

        case 3:
           q = 0
           for j in range(line  , 0, -2 ):            
            print(' ' * q  , end=' ')
            q += 2
            for i in range( 1, j + 1  ):
                
                print( "*" , end=" ")
            print()

        case 4:
            q = line - 1
            for j in range(1, line +1, 2):
                print(' ' * q , end='')
                q -= 2            
                for i in range(1, j + 1 ):
                    print( '*' , end=" ")
                print()

        case 5:
            q = 0
            for j in range(line  , 1, -2 ):            
                print(' ' * q  , end=' ')
                q += 2
                for i in range( 1, j + 1  ):                        
                    print( "*" , end=" ")
                print() 

            q = line  
            for j in range(1, line +1, 2):
                
                print(' ' * q , end='')
                q -= 2            
                for i in range(1, j + 1 ):
                    print( '*' , end=" ")
                print() 
           
        # case 6:

                 
