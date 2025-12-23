def run():
    print("Neon Terminal – wpisz 'exit' aby wyjść")
    while True:
        cmd = input(">>> ")
        if cmd.lower() == "exit":
            break
        try:
            exec(cmd)
        except Exception as e:
            print(f"Błąd: {e}")

