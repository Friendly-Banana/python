import sys, random, time
from string import ascii_lowercase as LOW_LETTERS, ascii_uppercase as BIG_LETTERS

SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890'

def write(message, end='\n'):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.randint(4, 10) / 1000)
    sys.stdout.write(end)

def cryptic(length=None):
    cryptics = ''
    if length == None:  # zufälliger Standardwert für Zeichenlänge
        length = random.randint(10, 80)
    for _ in range(length): # zufällige Zeichen
        cryptics += random.choice(SYMBOLS)
        if random.randint(0, 9) == 9:
            cryptics += random.choice(' ')
    return cryptics

def bits(length=250):
    global x, lx
    string, x  = '', 12
    for _ in range(length):
        string += random.choice(('0', '1'))
        if len(string) > x:
            x += 12
            if random.randint(0, 5) == 5:
                string += '\n'
        lx = len(string)
    return string#, x, lx

def word(length=None):
    word = ''
    if length == None:  # zufälliger Standardwert für Wortlänge
        length = random.randint(2, 7)
    if random.randint(0, 1) == 1:  # zufällig, ob das Wort mit Klein- oder Großbuchstabe beginnt
        word += random.choice(BIG_LETTERS)
        length += 1
    for _ in range(length): # zufällige Buchstaben
        word += random.choice(LOW_LETTERS)
    return word

def random_text(length=100):
    text = ''
    for _ in range(length):
        text += word()
        if random.randint(0, 9) == 9:
            text += random.choice('.,!?')
        text += ' '
    text += text[:-1] + random.choice('.!?')

    return text

def obfuscate(length=250): # not really
    text = ''
    for _ in range(length):
        text += random.choice((BIG_LETTERS+LOW_LETTERS+SYMBOLS+' \n\t'+word()))

    return text

#write(obfuscate())
write(random_text())
#write(bits())
#write(cryptic())
