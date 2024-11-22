def handshakes(peoples):
    for p in len(peoples):
        people = peoples[0]
        print(f"{people} handshake {peoples[p + 1]}")
        people += 1
        p += 1


handshakes(['Alice', 'Bob'])
# printHandshakes(['Alice', 'Bob', 'Carol'])
# printHandshakes(['Alice', 'Bob', 'Carol', 'David'])