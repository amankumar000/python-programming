print('''                               
                                    *******NUMBER GUESSING GAME \U0001F920*******


                             IN THIS GAME YOU HAVE TO CHOSE A NUMBER BETWEEN 1 TO 31

                                    COMPUTER WILL SHOW YOU SOME LIST  OF NUMBER  

                JUST YOUR HAVE TO SAY YES OR NO WHEN YOUR NUMBER IS PRESENT IN THAT LIST OR NOT.

                                         LETS START THE GAME \U0001F920''')
a = int(input("PRESS 1 TO START THE GAME"))
if a == 1:
    g = 0
    print(''' 1
                                        GUESS ANY ONE NUMBER FROM 1 TO 31''')

    print('''                            

                                      TYPE Y IF YOU HAVE GUESSED       ''')
    b = input()
    if b == 'y':
        print(f'''                   
                                       IS YOUR GUESSED NUMBER IS PRESENT IN THE GIVEN LIST 


                                [16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31]

                                                    ''')
        c = input('''
                              PRESS Y : "YES
                              PRESS N : NO


                            ''')
        if c == 'y':
            g = g + 16
        else:
            g = g + 0

        print(f'''                         
                                             IS YOUR GUESSED NUMBER IS PRESENT IN THE GIVEN LIST 


                                        [8  9  10  11  12  13  14  15  24  25  26  27  28  29  30  31]

                                                           ''')
        f = input('''
                                      PRESS Y : "YES
                                      PRESS N : NO
                                      ''')
        if (f == 'y'):
            g = g + 8
        else:
            g = g + 0

        print(f'''                          
                                   IS YOUR GUESSED NUMBER IS PRESENT IN THE GIVEN LIST 



                             [4  5  6  7  12  13  14  15  20  21  22  23  28  29  30  31]

                                                                   ''')
        h = input('''
                                              PRESS Y : "YES
                                              PRESS N : NO
                                              ''')
        if h == 'y':
            g = g + 4
        else:
            g = g + 0

        print(f'''                        
                               IS YOUR GUESSED NUMBER IS PRESENT IN THE GIVEN LIST 


                        [2  3  6  7  10  11  14  15  18  19  22  23  28  29  30  31]

                                                                   ''')
        j = input('''
                                              PRESS Y : "YES
                                              PRESS N : NO
                                              ''')
        if j == 'y':
            g = g + 2
        else:
            g = g + 0

        print(f'''                          
                                    IS YOUR GUESSED NUMBER IS PRESENT IN THE GIVEN LIST 


                            [1  3  5  7  9  11  13  15  17  19  21  23  25  27  29  31]
                                                                   ''')
        k = input('''
                                              PRESS Y : "YES
                                              PRESS N : NO
                                              ''')
        if k == 'y':
            g = g + 1
        else:
            g = g + 0

        print('''  1

                                         DO YOU WANT TO SEE THE MAGIC \U0001F920  : PRESS 1''')
        d = int(input())
        if d == 1:
            print(F'''

                                          ***** YOUR GUSSED NUMBER IS    : {g}  *****''')

