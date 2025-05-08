from time import sleep as pleaseWait

def animateText(text, delay = 0.05):
    for char in text:
        print(char, end = '', flush = True)
        pleaseWait(delay)
    print()