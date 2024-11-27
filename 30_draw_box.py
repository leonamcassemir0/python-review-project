def draw_box(boxes):
    if boxes == 0:
        return print(None)

    print(' ' * (boxes + 1) + "+" + "-" * (boxes * 2) + "+")
    for b in range(boxes):
        print(" "*(boxes - b) + "/" + " "*(boxes * 2) + "/" + " "*(b) + "|" )
    
    print("+" + "-"*(boxes * 2) + "+" + " "*(boxes) + "+")

    for i in range(boxes):
        print("|" + " "*(boxes * 2) + "|" + " "*(boxes - i) + "/")
        
    print("+" + "-" * (boxes * 2) + "+")


for x in range(6):
    print(f"Caixa com {x} niveis:")
    draw_box(x)
    print()