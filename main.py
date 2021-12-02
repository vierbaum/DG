import argparse
import numpy

vars = [[], []]

parse = argparse.ArgumentParser()
parse.add_argument("-s")
args = parse.parse_args()

file1 = open(args.s, 'r')
Lines = file1.readlines()


def dec_num(num):
    try:
        return float(num)
    except:
        ValueError

    if num in vars[0]:
        return vars[1][vars[0].index(num)]

def write_to_var(params):
        if params[1] in vars[0]:
            vars[1][vars[0].index(params[1])] = dec_num(params[2])
        else:
            vars[0].append(params[1])
            vars[1].append(float(params[2]))

def operate(params):
    # calculate
    if params[0] == "+":
        print(dec_num(params[1]) + dec_num(params[2]))

    if params[0] == "-":
        print(dec_num(params[1]) - dec_num(params[2]))

    if params[0] == "*":
        print(dec_num(params[1]) * dec_num(params[2]))

    if params[0] == "/":
        print(dec_num(params[1]) / dec_num(params[2]))

    if params[0] == "%":
        print(dec_num(params[1]) % dec_num(params[2]))

    # vars
    if params[0] == "v":
        if params[2] == "o":
            if params[3] == "+":
                write_to_var([0, params[1], (dec_num(params[4]) + dec_num(params[5]))])

            if params[3] == "-":
                write_to_var([0, params[1], (dec_num(params[4]) - dec_num(params[5]))])

            if params[3] == "*":
                write_to_var([0, params[1], (dec_num(params[4]) * dec_num(params[5]))])

            if params[3] == "/":
                write_to_var([0, params[1], (dec_num(params[4]) / dec_num(params[5]))])

            if params[3] == "%":
                write_to_var([0, params[1], (dec_num(params[4]) % dec_num(params[5]))])

        else:
            write_to_var(params)

    if params[0] == "p":
        print(dec_num(params[1]))

    if params[0] == "l":
        progs = params.split("&")
        new_code = []
        for i in progs:
            new_code.append(i.split(" "))
        var = new_code[0][1].split(",")

        for i in range(int(var[0]), int(var[1]), int(var[2])):
            for l in range(len(new_code)):
                if new_code[l][0] == "l":
                    write_to_var([0, new_code[l][2], i])
            for l in range(len(new_code)):
                operate(new_code[l][(3 - len(new_code[l])):])

    # logical
    if params[0] == "<":
        if dec_num(params[1]) < dec_num(params[2]):
            operate(params[(3 - len(params)):])

    if params[0] == ">":
        if dec_num(params[1]) > dec_num(params[2]):
            operate(params[(3 - len(params)):])

    if params[0] == "=":
        if dec_num(params[1]) == dec_num(params[2]):
            operate(params[(3 - len(params)):])

    if params[0] == "!=":
        if dec_num(params[1]) != dec_num(params[2]):
            operate(params[(3 - len(params)):])

for line in Lines:
    if "&" in line.strip():

        operate(line.strip())
        try:
            pass
        except:
            IndexError
    else:
        try:
            code = line.strip().split(" ")
            operate(code)
        except:
            IndexError

