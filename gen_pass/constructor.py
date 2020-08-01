#!/usr/bin/python

from random import randint
import string, sys
import numpy as np
import getopt


def main(argv):
    pars = {'length': 32, 'symbol': True, 'number': True, 'lowercase': True, 'uppercase': True, 'name': ""}
    try:
        opts, args = getopt.getopt(argv, "n:l:s:r:c:u:",
                                   ["name", "length", "symbol", "number", "lowercase", "uppercase"])
    except getopt.GetoptError:
        print
        'generate.py -n <name> -l <length> -s <symbol> -r <number> -c <lowercase> -u <uppercase>'
        sys.exit(2)
    if len(opts) == 0:
        print
        generate(**pars)
        sys.exit()
    for opt, arg in opts:
        dic = {'-n': "name",
               '-l': "length",
               '-s': "symbol",
               '-r': "number",
               '-c': "lowercase",
               '-u': "uppercase"}
        if opt == '-l':
            arg = int(arg)
        pars[dic[opt]] = arg

    password = generate(**pars)

    print
    "password:", password


def generate(length, symbol=True, number=True, lowercase=True, uppercase=True, name=""):
    chars = {"symbol": ['@', '%', '#', '$'] if symbol else [],
             "number": map(str, range(0, 10)) if number else [],
             "lowercase": list(string.lowercase) if lowercase else [],
             "uppercase": list(string.uppercase) if uppercase else []}

    symbols = np.array(['@', '%', '#', '$'])
    numbers = map(str, range(0, 10))
    lowercases = list(string.lowercase)
    uppercases = list(string.uppercase)

    possiblechars = []
    for par in chars:
        if par:
            possiblechars += chars[par]
    xs = [randint(0, len(possiblechars) - 1) for p in range(length)]
    possiblechars = np.array(possiblechars)
    password = possiblechars[xs]
    password = ''.join(password)

    with open("passwords.txt", "a+") as f:
        f.write("\n" + name + ": " + password)
    return password


if __name__ == "__main__":
    main(sys.argv[1:])