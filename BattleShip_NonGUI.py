# Author Jordan Lake
# class create_player creates a template to make a player
class Create_player:
    # creates a global variable sp = the ascii value of sp/space
    global sp
    sp = chr(32)

    # This function lets you choose what player you are.
    def choose_player():
        # asks what player you are.
        player = input("Which player are you, 001, 011, 111")
        print(player)
        # returns the value of player
        return player

    # sets up the board for the player
    def set_Map():
        # asks you for you first row
        global row1
        row1 = input("Please input your first row, exapmle: 010. a 1 is where your ship is")
        # asks you for you second row
        global row2
        row2 = input("Please input your secon row, exapmle: 010. a 1 is where your ship is")
        # asks you for you third row
        global row3
        row3 = input("Please input your third row, exapmle: 010. a 1 is where your ship is")
        print(row1 + sp + row2 + sp + row3)


# Creates the class to start actually play the game
class Game:
    # Set the number of player
    def players(self):
        # Creates the global variable amount_of_players
        global amount_of_players
        # Asks how many players are gonna play and set amount_of_players to the number they input
        amount_of_players = input("How many players do you have?")

    # Creates the objects that each player needs to play the game
    def if_players(self):
        # Calls the player function so you can use the vaiable amount_of_players
        Game.players()
        # Checks to see if the amount of players is 1
        if amount_of_players == "1":
            # If so print that you need friends to play this game
            print("You need friends to play this game.")
        # Checks to see if the amount of players is 2
        elif amount_of_players == "2":
            # Creates objects for the players positions and maps
            global player1_position
            player1_position = Create_player.choose_player()
            global player1_map
            player1_map = Create_player.set_Map()
            global player2_position
            player2_position = Create_player.choose_player()
            global player2_map
            player2_map = Create_player.set_Map()

    # Creates the function used to attack other players
    @staticmethod
    def attack():
        # Prints how to attack
        print(
            "This is the attack phase of the game. To attack you will be give three rows to place one shot in. A 1 is "
            "considered a shot")
        # Askes where you want to attack in the first row
        global attack_row1
        attack_row1 = input("Row one:")
        # Askes where you want to attack in the second row
        global row2
        attack_row2 = input("Row two:")
        # Askes where you want to attack in the second row
        global row3
        attack_row3 = input("Row three:")

    def hit_or_miss():
        Game.attack()
        Game.if_players()
        while amount_of_players == "2":
            if attack.attack_row1 == if_players.player1_map.row1:
                print("Hit")


class main():
    Game.if_players()


main()
