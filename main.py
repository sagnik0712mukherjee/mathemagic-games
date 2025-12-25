import sys
from src.games.snake import run_snake_game
from src.games.rps import start_game as run_rps
from src.math_tools.complex import analyze_complex, complex_math_ops
from src.math_tools.quadratic import solve_quadratic
from src.math_tools.fractions import decimal_to_fraction
from src.math_tools.pythagoras import find_triplets
from src.logic.pie_share import calculate_highest_share

def main():
    print("="*30)
    print("Welcome to Mathemagic Games!")
    print("="*30)
    print("1. Snake Q-Learning Game")
    print("2. Stone Paper Scissor")
    print("3. Complex Number Analyzer")
    print("4. Quadratic Equation Solver")
    print("5. Decimal to Fraction Converter")
    print("6. Pythagorean Triplets Finder")
    print("7. Pie Share Calculator")
    print("8. Complex Arithmetic (Add/Sub/Mul/Div)")
    print("0. Exit")
    print("="*30)
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        run_snake_game()
    elif choice == '2':
        run_rps()
    elif choice == '3':
        z = input("Enter a complex number (e.g., 2 + 12i): ")
        analyze_complex(z)
    elif choice == '4':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        solve_quadratic(a, b, c)
    elif choice == '5':
        num = float(input("Enter a decimal number: "))
        decimal_to_fraction(num)
    elif choice == '6':
        lower = int(input("Enter lower bound: "))
        upper = int(input("Enter upper bound: "))
        find_triplets(lower, upper)
    elif choice == '7':
        calculate_highest_share()
    elif choice == '8':
        z1 = input("Enter first complex number (e.g., 2 + 12i): ")
        z2 = input("Enter second complex number (e.g., 1 - i): ")
        results = complex_math_ops(z1, z2)
        print("\nResults:")
        for op, val in results.items():
            print(f"  {op}: {val}")
    elif choice == '0':
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        main()
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break
