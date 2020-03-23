def pos(v):
    return ord(v) - ord('A') + 1

def vowel(v):
    if pos(v)==5 or pos(v)==9 or pos(v)==1 or pos(v)==15 or pos(v)==21:
        return 1
    else:
        return 0
def minion_game(string):
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if vowel(s[i])==1 :
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin>stuart:
        print("Kevin " + str(kevin))
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart " + str(stuart))
if __name__ == '__main__':
    s = input()
    minion_game(s)

