"""
    collatz(10) → [10, 5, 16, 8, 4, 2, 1]

    The Collatz Sequence also called the 3n + 1 problem, is a simple but mysterious numeric 
    sequence that has remained unsolved by mathematicians. It has four rules:
    - Begin with a positive, nonzero integer called n.
    - If n is 1, the sequence terminates.
    - If n is even, the next value of n is n / 2.
    - If n is odd, the next value of n is 3n + 1
"""

def collatz(value):
    collatz = [value]
    num = value
    
    while num != 1:
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num = num // 2
        
        collatz.append(num)

    return collatz

print(collatz(10))
print(collatz(1))
