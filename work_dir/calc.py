import math
import sys
sys.path.append("./work_dir")

from common_functions import write_out_history, get_number, read_history

def calc_main_func():
    print("Tryb kalkulator. Wpisz 'q' żeby wyjść ;)")

    while True:
        operator = input("Choose an operator (+, -, *, /, !, ^, q): ").strip()

        if operator == 'q':
            break

        if operator in ['+', '-', '*', '/', '^']:
            num1 = get_number("Pierwsza liczba: ")
            num2 = get_number("Druga liczba: ")


            if operator == '-':
                result = num1 - num2
            elif operator == '+':
                result = num1 + num2
            elif operator == '/':
                if num2 == 0:
                    print("There is impossible assertion!")
                    continue
                result = num1 / num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '^':
                result = num1 ** num2

        elif operator == '!':
            num1 = int(get_number("Integer number"))
            if num1 < 0:
                print("We cannot do this operation on the negative number!")
                continue
            result = math.factorial(num1)

        else:
            print("I didn't get this operator")
            continue

        print(f"Wynik końcowy to {result}")

        if operator == '!':

          write_out_history(operator, [num1], result)
        else:
          write_out_history(operator, [num1, num2], result)


        if operator == 'h':
            history = read_history()
            if history:
                print("Historia działań:")
                for elem in history:
                    print(elem.strip())
            continue

if __name__ == "__main__":
    calc_main_func()

