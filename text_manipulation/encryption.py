import string, random

abc = string.printable
swap_abc = ''.join(random.sample(string.printable, len(string.printable)))

def swap_en(ip : str) -> str:
    return ''.join(swap_abc[abc.index(char)] for char in ip)

def swap_de(ip : str) -> str:
    return ''.join(abc[swap_abc.index(char)] for char in ip)
    
def caesar_en(ip : str) -> str:
    return ''.join(abc[-abc.index(char) + 13] for char in ip)
    
def caesar_de(ip : str) -> str:
    return ''.join(abc[-abc.index(char) + 13] for char in ip)
    
e = caesar_en(input())
print(e)
print(caesar_de(e))