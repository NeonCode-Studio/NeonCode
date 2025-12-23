from apps.calculator import main as calc
from apps.notepad import main as notepad
from apps.clock import main as clock
from apps.phone import main as phone

apps = ["Calculator", "Notepad", "Clock", "Phone"]

def list_apps():
    print("\nDostępne aplikacje:")
    for i, app in enumerate(apps, 1):
        print(f"{i}. {app}")

def launch_app(choice):
    if choice == 1:
        calc.run()
    elif choice == 2:
        notepad.run()
    elif choice == 3:
        clock.run()
    elif choice == 4:
        phone.run()
    else:
        print("Niepoprawny wybór.")

def main():
    while True:
        list_apps()
        try:
            choice = int(input("Wybierz aplikację (0 aby wyjść): "))
            if choice == 0:
                print("Zamykanie NeonCode...")
                break
            launch_app(choice)
        except ValueError:
            print("Podaj liczbę!")

if __name__ == "__main__":
    main()
