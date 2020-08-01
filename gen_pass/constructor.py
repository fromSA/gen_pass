#!/usr/bin/python

import getopt
import string
import sys
from random import randint
import numpy as np


def main(argv):
    pars = {'length': 32, 'symbol': True, 'number': True, 'lowercase': True, 'uppercase': True, 'name': ""}
    try:
        opts, args = getopt.getopt(argv, "n:l:s:r:c:u:",
                                   ["name", "length", "symbol", "number", "lowercase", "uppercase"])
    except getopt.GetoptError:
        print('generate.py -n <name> -l <length> -s <symbol> -r <number> -c <lowercase> -u <uppercase>')
        sys.exit(2)
    if len(opts) == 0:
        print(generate(**pars))
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

    print("password:", password)


def generate(length, symbol=True, number=True, lowercase=True, uppercase=True, name=""):
    chars = {"symbol": ['@', '%', '#', '$'] if symbol else [],
             "number": map(str, range(0, 10)) if number else [],
             "lowercase": list(string.lowercase) if lowercase else [],
             "uppercase": list(string.uppercase) if uppercase else []}

    symbols = np.array(['@', '%', '#', '$'])
    numbers = map(str, range(0, 10))
    lower_cases = list(string.lowercase)
    upper_cases = list(string.uppercase)

    possible_chars = []
    for par in chars:
        if par:
            possible_chars += chars[par]
    xs = [randint(0, len(possible_chars) - 1) for _ in range(length)]
    possible_chars = np.array(possible_chars)
    password = possible_chars[xs]
    password = ''.join(password)

    with open("passwords.txt", "a+") as f:
        f.write("\n" + name + ": " + password)
    return password


if __name__ == "__main__":
    main(sys.argv[1:])
