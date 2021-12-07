import argparse
import re
import numpy

vars = [[], []]
parse = argparse.ArgumentParser()
parse.add_argument("-s")
Lines = open(parse.parse_args().s, 'r').readlines()

def dec_num(num):
    if num in vars[0]: return vars[1][vars[0].index(num)]
    else: return float(num)

def write_to_var(params):
    if params[2] == "[]":
        vars[0].append(params[1])
        vars[1].append([])

    elif params[1] in vars[0]: vars[1][vars[0].index(params[1])] = dec_num(params[2])
    else:
        vars[0].append(params[1])
        vars[1].append(dec_num(params[2]))

def operate(params):
    if params[0] == "v":
        if params[2] == "o":
            if params[3] == "+": write_to_var([0, params[1], (dec_num(params[4]) + dec_num(params[5]))])
            if params[3] == "-": write_to_var([0, params[1], (dec_num(params[4]) - dec_num(params[5]))])
            if params[3] == "*": write_to_var([0, params[1], (dec_num(params[4]) * dec_num(params[5]))])
            if params[3] == "/": write_to_var([0, params[1], (dec_num(params[4]) / dec_num(params[5]))])
            if params[3] == "%": write_to_var([0, params[1], (dec_num(params[4]) % dec_num(params[5]))])
            if params[3] == "^": write_to_var([0, params[1], (dec_num(params[4]) ** dec_num(params[5]))])
            if params[3] == "g": write_to_var([0, params[1], vars[1][vars[0].index(params[4])][int(dec_num(params[5]))]])
        else:
            write_to_var(params)

    if params[0] == "l":
        new_code = [params[0:params.index("&")].split(" "), params[params.index("&") + 1:]]
        for i in range(int(dec_num(new_code[0][1].split(",")[0])), int(dec_num(new_code[0][1].split(",")[1])), int(dec_num(new_code[0][1].split(",")[2]))):
            write_to_var([0, new_code[0][2], i])
            operate(new_code[1]) if new_code[1][0] == "l" else [operate([i for i in re.split(r' |(?<=")(.*)(?=")', j) if i != "\"" and i != None]) for j in new_code[1].split("&")]

    if params[0] == "<" and dec_num(params[1]) < dec_num(params[2]): operate(params[(3 - len(params)):])
    if params[0] == ">" and dec_num(params[1]) > dec_num(params[2]): operate(params[(3 - len(params)):])
    if params[0] == "=" and dec_num(params[1]) == dec_num(params[2]): operate(params[(3 - len(params)):])
    if params[0] == "!" and dec_num(params[1]) != dec_num(params[2]): operate(params[(3 - len(params)):])
    if params[0] == "a": vars[1][vars[0].index(params[1])].append(dec_num(params[2]))
    if params[0] == "s": vars[1][vars[0].index(params[1])][int(params[2].split(",")[0])] = dec_num(params[2].split(",")[1])
    if params[0] == "p": print(params[1].format(*[dec_num(x) for x in params[2].split(",")]))
    if params[0] == "g": print(vars[1][vars[0].index(params[1])][int(dec_num(params[2]))])

for line in Lines: operate(line.strip()) if line.strip()[0] == "l" else operate([i for i in re.split(r' |(?<=")(.*)(?=")', line.strip()) if i != "\"" and i != None])
