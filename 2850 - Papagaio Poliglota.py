while True:
    try:
        n = input()

        if n == "esquerda":
            print("ingles")
        elif n == "direita":
            print("frances")
        elif n == "nenhuma":
            print("portugues")
        else:
            print("caiu")
    except EOFError as e:
        break