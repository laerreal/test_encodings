#!/usr/bin/python

from sys import executable
from os.path import split, join
from os import listdir
from re import compile
from subprocess import Popen

re_interpreter = compile("python[0-9]+\.[0-9]+$")

if __name__ == "__main__":
    # https://stackoverflow.com/a/5927643/7623015
    print("Interpreter: " + executable)

    # find out all available interpreters
    intrerpreters = []
    i_dir = split(executable)[0]
    for n in listdir(i_dir):
        if re_interpreter.match(split(n)[1]):
            intrerpreters.append(join(i_dir, n))

    print("Available interpreters: " + ", ".join(intrerpreters))

    tester = join(split(__file__)[0], "test_encodings.py")

    for i in intrerpreters:
        args = [i, tester]
        print("Launching " + " ".join(args))
        launch = Popen(args)
        launch.wait()
