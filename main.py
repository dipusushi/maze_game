print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888(FL)888
''')
print("Welcome to Crossroads Mall Maze.")
print ("Main goal of this game is to find an exit door!")


choice_1 = input ('Your\'e at the Crossroads Mall entrance, where do you want to go? Type "left" or "right".\n').lower()

if choice_1 == "right":
          choice_2 = input("You've come to Food Court. There is a Subway and Panda Express in there. Type \"subway\" to go to subway. Type \"panda\" to go to panda express.\n").lower()
          if choice_2 == "panda":
                    choice_3 = input("You have reached the Panda Express. There is a red key,  blue key and a yellow key. Which colour do you choose?\n").lower()
                    if choice_3 == "red":
                              print('"WOMP WOMP" You opened a door to a ferocious panda cage. Game Over!')
                    elif choice_3 == "blue":
                              print("You found the exit door! You Win!")
                    elif choice_3 == "yellow":
                              print ('"WOMP WOMP" You entered dishwashing room, now do the dishes. Game Over!')
                              
                    
                    else:
                              print("You chose a door that doesn't exist. Game Over.")
          else:
                    print ('"WOMP WOMP" You just ate sandwich and died. Game Over')
else:
          print ('"WOMP WOMP" You fell into the sewers canal. Game Over!')