import random

#Global constants
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1
ROWS = 3 
COLS = 3 

symbols = {"🥰":3,"🍒":4,"🍋":6,"🍌":8}   #frequency of the symbols
symbols_value = {"🥰":5, "🍒":4, "🍋":2, "🍌":1}    

#user input 
def deposit():
    while True:
        amount = input("Enter the amount you'd like to deposit : $")
        if amount.isdigit():    #check if the input is actually a number
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Please enter a number.")
    return amount 

def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():   
            lines = int(lines)
            if(1 <=  lines <= MAX_LINES):
                break
            else:
                print("Enter a valid number of lines !")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? : $")
        if bet.isdigit():    #check if the input is actually a number
            bet = int(bet)
            if(MIN_BET <= bet <= MAX_BET):
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}!")
        else:
            print("Please enter a number.")
    return bet

def get_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_spin(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i != len(col)-1:
                print(col[row],end=" | ")
            else:
                print(col[row], end = "")
        print()
     
def check_winnings(columns, lines, bet, values):
    winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break 
        
        else:
            winnings += values[symbol]*bet 
            winning_lines.append(line+1)
    return winnings, winning_lines

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"You do not have sufficient balance. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${bet*lines}")
    
    slots = get_spin(ROWS, COLS, symbols)
    print_slot_spin(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbols_value)
    print(f"You won ${winnings}.")
    print("You won on lines: ",*winning_lines)
    return winnings-total_bet 
    
def main():
    print("**************************************")
    balance = deposit()
    while balance:
        print(f"Your current balance is: ${balance}")
        print("---------------------------------------")
        ans = input("Press enter to play (q to quit).")
        if ans == "q":
            break 
        balance += spin(balance)
        
    print(f"You left with ${balance}.")
    print("**************************************")

main()

