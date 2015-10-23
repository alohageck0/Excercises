G = ['7283455864',
     '6731158619',
     '8911111142643',
     '3830589324',
     '131111111111112',
     '5633845374',
     '6473530293']

P = ['1111',
     '5374',
     '0293']

arr = []


def find_characters(strin, pattern):
    """
    Returns array of indexes of first row of pattern
    :param strin:
    :param pattern:
    :return:
    """
    found = []
    last_index = -1
    while True:
        try:
            last_index = strin.index(pattern, last_index + 1)
        except ValueError:
            break
        else:
            found.append(last_index)
    return found
