def run():
    print("Binary-to-Text Translator")
    print("Wpisz binarny ciąg (np. 01001000 01101001) lub 'exit' aby wyjść.")
    
    while True:
        binary_input = input("Binary: ").strip()
        if binary_input.lower() == "exit":
            break
        try:
            text = "".join([chr(int(b, 2)) for b in binary_input.split()])
            print(f"Text: {text}")
        except ValueError:
            print("Niepoprawny format binarny. Podaj ciąg 0 i 1 oddzielony spacją.")
