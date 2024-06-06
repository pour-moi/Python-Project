print('''
     ___________
           / |       | |
        ,' ,'         \/',_    __
     ,'__/             |    ',|  "'-,,,,,,,
   ,/  _|',            |                |   \
   |  |   |',           \               |    \
   |__|   |  ',          ',             |     \
  /       |     ',        ,_"""""---'-_,'______\
 /        |        ',,_-'"    |        |        ',
|_________|         |         /        |        / ',,'""""|
|__  |        ,____/         |        _|       /    |___  /
'\___|      ,'_,'|_,-,_______|         |       /      , '/
  \,' _', _/  ,, ,',|        |          \       |   '" ,'
   \ / |_ ,  |  \||||       ,' |      ,'|    _""    |,'
    ' ,'  ', |  ||||| __ ,'   _|_ ,'    |    |""---/
       ' ,"""','"""""" |     /           \"""|    /
                      |_____|_      __''"    \   |
                     |  |  /  """"""   |      \ /
                      \ / |            |       /
                       \--'            |      /
                       |   \__        _|__    |
                       |      |__     |   ',,,|
                       |         |____|   /   |
                       /         _|    ,,'_   |
                      |__________|___,'  ,,' /
                       \      ---'    \,/  ,'
                        \     |    ,,,' \_/
                         |    |_,''      |/
                         |    |       []_|
                          \___'        /
                           \       __,'
                            \_____/ 
      ''')

print("Welcome to the treasure island. Your mission is to find the treasure")
choose_direction = input("You're at a cross road. Where do you want to go? left or right ").lower()
if choose_direction == "left":
    choose_preference = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ").lower()
    if choose_preference == "wait":
        choose_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one Yellow and one blue. Which color do you choose? ").lower()
        if choose_door == "yellow":
            print("You Win!")
        elif choose_door == "red":
            print("Burned by fire. Game Over")
        elif choose_door == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game over")

else:
    print("Fall in to a hole. Game Over")