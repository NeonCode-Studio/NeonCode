import os

def run():
    print("NeonCommander – prosty menedżer plików")
    path = os.getcwd()  # ustawiamy absolutny katalog startowy
    while True:
        print("\nAktualny katalog:", os.path.abspath(path))
        try:
            contents = os.listdir(path)
        except FileNotFoundError:
            print("Nie można odczytać katalogu!")
            path = os.getcwd()
            continue

        print("Zawartość:", contents)
        cmd = input("Polecenie (cd [folder]/exit): ").strip()
        if cmd.lower() == "exit":
            break
        elif cmd.startswith("cd "):
            folder = cmd[3:].strip()
            new_path = os.path.join(path, folder)
            if os.path.isdir(new_path):
                path = os.path.abspath(new_path)
                os.chdir(path)
            else:
                print("Nie ma takiego folderu!")
