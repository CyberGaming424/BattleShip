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


class Game:
    # Set the number of player
    def players(self):

        # Asks how many players are gonna play and set amount_of_players to the number they input
        self.amount_of_players = input("How many players do you have?")

    # Creates the objects that each player needs to play the game
    def if_players(self):
        # Calls the player function so you can use the vaiable amount_of_players
        # Checks to see if the amount of players is 1
        if self.amount_of_players == "1":
            # If so print that you need friends to play this game
            print("You need friends to play this game.")
        # Checks to see if the amount of players is 2
        elif self.amount_of_players == "2":
            # Creates objects for the players positions and maps
            def player1_position(self):
                self.player1_position = Create_player.choose_player()
            self.player1_map = Create_player.set_Map()
            self.player2_position = Create_player.choose_player()
            self.player2_map = Create_player.set_Map()


    # Creates the function used to attack other players

    def hit_or_miss(self):
        while self.amount_of_players == "2":
            if self.attack_row1 == self.if_players.player1_map.row1:
                print("Hit")



class Main():
    game1 = Game()
    Game.players()


Main()
