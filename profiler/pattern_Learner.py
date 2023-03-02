import pandas as pd

patterns = []
patterns1 = []
patterns2 = []
patterns3 = []


# Syntactically learn patterns
def learn_patterns(input1):
    patterns.clear()
    patterns1.clear()
    patterns2.clear()
    patterns3.clear()
    for l in input1:
        pi = ''  # U/l/d/' '/sp.char # Top Pattern
        pi1 = ''  # s/d/./S # Data pattern
        pi2 = ''  # s/d/S  # DMV
        pi3 = '' # s/d/sp.char # Date pattern

        if pd.isnull(l):
            pi = ''
            pi1 = ''
            pi2 = ''
            pi3 = ''
            patterns.append(pi)
            patterns1.append(pi1)
            patterns2.append(pi2)
            patterns3.append(pi3)
        else:
            l = str(l)

            for l1 in l:
                if l1 in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z']:
                    p = 'l'
                    pi = pi + p
                    p1 = 's'
                    pi1 = pi1 + p1
                    pi2 = pi2 + p1
                    pi3 = pi3 + p1
                    # pattern.append(p)
                elif l1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S',
                            'T',
                            'U', 'V', 'W', 'X', 'Y', 'Z']:
                    p = 'U'
                    pi = pi + p
                    p1 = 's'
                    pi1 = pi1 + p1
                    pi2 = pi2 + p1
                    pi3 = pi3 + p1
                    # pattern.append(p)
                elif l1 in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    p = 'd'
                    pi = pi + p
                    p1 = 'd'
                    pi1 = pi1 + p1
                    pi2 = pi2 + p1
                    pi3 = pi3 + p1
                    # pattern.append(p)
                elif l1 == ' ':
                    p = ' '
                    pi = pi + p
                    p1 = ''
                    pi1 = pi1 + p1
                    pi2 = pi2 + p
                    p2 = ''
                    pi3 = pi3 + p2
                    # pattern.append(' ')
                elif l1 =='.':
                    pi = pi + l1
                    pi1 = pi1 + l1
                    pi2 = pi2 + l1
                    p2 = 'S'
                    pi3 = pi3 + p2
                    # pattern.append(' ')
                else:
                    pi = pi + l1
                    p1 = 'S'
                    pi1 = pi1 + p1
                    pi2 = pi2 + l1
                    pi3 = pi3 + p1
                    # pattern.append(l)
            # print(pi)
            #print(patterns2)
            patterns.append(pi)
            patterns1.append(pi1)
            patterns2.append(pi2)
            patterns3.append(pi3)

    #print(patterns2, len(patterns2))
    return patterns, patterns1, patterns3, patterns2
