"""
cli.py - command-line menu for the ancient Aryabhatiya algorithms.
Run:  python cli.py
"""
from ancient_algorithms import kuttaka_modular_inverse, aryabhata_square_root, aryabhata_cube_root
from modern_checks import modern_inverse, modern_sqrt, modern_cbrt


def menu():
    print("\n===================================================")
    print(" ARYABHATIYA COMPUTATIONAL ALGORITHMS - CLI")
    print("===================================================")
    print(" 1. Kuttaka  -> find modular inverse of b mod a")
    print(" 2. Square Root (Varga method)")
    print(" 3. Cube Root (Ghana/Aghana method)")
    print(" 0. Exit")
    return input("Choose an option (0-3): ").strip()


def show(title, steps, ancient, modern, extra=""):
    print(f"\n--- Ancient Method ({title}) Step Trace ---")
    print("\n".join(steps))
    print(f"\nAncient result : {ancient}{extra}")
    print(f"Modern check   : {modern}")
    print("MATCH ✔" if ancient == modern else "MISMATCH ✘")


def run_kuttaka():
    b = int(input("Enter b (number to invert): "))
    a = int(input("Enter a (modulus): "))
    try:
        inv, steps = kuttaka_modular_inverse(b, a)
    except ValueError as e:
        print(f"\n[!] {e}")
        return
    show("Kuttaka / Valli", steps, inv, modern_inverse(b, a))


def run_sqrt():
    n = int(input("Enter a positive integer n: "))
    root, rem, steps = aryabhata_square_root(n)
    show("Varga", steps, root, modern_sqrt(n), f"  (remainder {rem})")


def run_cbrt():
    n = int(input("Enter a positive integer n: "))
    root, rem, steps = aryabhata_cube_root(n)
    show("Ghana/Aghana", steps, root, modern_cbrt(n), f"  (remainder {rem})")


if __name__ == "__main__":
    actions = {"1": run_kuttaka, "2": run_sqrt, "3": run_cbrt}
    while True:
        choice = menu()
        if choice == "0":
            print("Goodbye.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option, try again.")
