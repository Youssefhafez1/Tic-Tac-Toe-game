class players :
    def __init__(self) :
        self.name = ""
        self.symbol = ""
    def choose_name(self):
        while True :
            name = input("Enter your name,please: ")
            if name.isalpha():
                self.name = name 
                break
            print("Invalid Name!")
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name},Enter your Fav. symbol: ")
            if symbol.isalpha() and len(symbol) == 1 :
                self.symbol = symbol 
                break
            print("Invalid Symbol!")
class menu:
    def start_menu(self):
        print("Welcome to X-O game!")
        print("""Choose from 1 & 2:
              1.Start game 
              2.End game""")
        choice = input("Enter:")
        return choice
    def end_menu(self):
        print("""Game over!
              1.Restart
              2.End game""")    
        choice = input("Enter:")
        return choice 
class borad:
    def __init__(self):
        self.borad = [str(i) for i in range(1,10)]
    def display_borad(self):
        for i in range(0,9,3):
            print("|".join(self.borad[i:i+3]))
            if i < 6 :
                print("-"*10)
    def update_board(self,choosen_place,symbol):
        if self.is_valid_move(choosen_place):
            self.borad[choosen_place - 1] = symbol
            return True
        return False
    def is_valid_move(self,choosen_place):
        return self.borad[choosen_place - 1].isdigit()    
    def reset_board(self):    
       self.borad = [str(i) for i in range(1,10)]
class game:
    def __init__(self):
        self.player = [players(),players()]        
        self.board = borad()
        self.menu = menu()
        self.current_player = 0
    def start_game(self):
        choice = self.menu.start_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else :
            self.quit_game()    
    def setup_players(self):
        for number, player in enumerate(self.player, start = 1 ):
            print(f"player{number}")
            player.choose_name()
            player.choose_symbol()
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                print(f"{self.player[1 - self.current_player].name} wins!")
                self.board.display_borad()
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            if self.check_draw():
                print("Draw!")
                self.board.display_borad()
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            
    def play_turn(self):
        player = self.player[self.current_player]
        self.board.display_borad()
        print(f"{player.name}'s turn ({player.symbol})")
        while True :
            try:
                cell_choice = int(input("Choose the wanted cell(1-9)"))
                if 1<=cell_choice<=9 and self.board.update_board(cell_choice,player.symbol):
                  break
                else:
                    print("Invalid Move")  
            except:
                print("Invalid Informations")
        self.switch_player()
    def switch_player(self):
        self.current_player = 1 - self.current_player            
    def check_win(self):
        for i in range(0,3):
            if self.board.borad[i] == self.board.borad[i+3] == self.board.borad[i+6]:
                return True 
        for i in range(0,7,3):
            if self.board.borad[i] == self.board.borad[i+1] == self.board.borad[i+2]:
                return True 
        if self.board.borad[0] == self.board.borad[4] == self.board.borad[8] or self.board.borad[2] == self.board.borad[4] == self.board.borad[6]:
            return True
        return False 
    def check_draw(self):
        x = 0
        if not self.check_win():
            for objs in self.board.borad :
                if objs.isalpha():
                    x += 1
            else : pass
        if x == 9 :
            return True 
        else : return False 
    def restart_game(self):
        self.board.reset_board()
        self.current_player = 0
        self.play_game()  
    def quit_game(self):
        print("Thanks for playing!")
game().start_game()
