# pylint: disable=superfluous-parens
import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    wins = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            wins += values[symbol]*bet
            win_lines.append(line + 1)

    return wins, win_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #columns = [[], [], []]
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns)-1:
                print(col[row],end = " | ")
            else:
               print(col[row], end ="") 
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit ? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 !")
        else:
            print("Please enter a number !")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Input number of lines you want to bet on Lines must be (1-"  + str(MAX_LINES) + ")? : ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid lines !")
        else:
            print("Please enter a number !")
    return lines

def get_bet():
    while True:
            amount = input("What would you like to bet on each line ? $: ")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
            else:
                print("Please enter a number !")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = lines*bet

        if total_bet > balance:
            print(f"You do not have suffivcient balance, your balance is: {balance}")
        else:
            break

    print(f"You are betting: ${bet} on line {lines}, your total bet is ${total_bet}")
    # print(balance, lines, bet)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won : {winnings} !!!")
    print(f"You won on lines: ,", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while(True):
        print(f"Current Balance Is : ${balance}")
        ans = input("Press Enter To Play (q to Quit)")
        if ans == 'q':
            break
        else:
            balance += spin(balance)
    print(f"You Left With: ${balance}")

main()
