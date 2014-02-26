#!/usr/bin/python
import json
import re
import random

MIN_CONS = 500
INFILE = 'lists'
OUTFILE = 'lists.json'


def crawl_list(user):
    if len(user) == 1:
        return
    working_list = user.pop(0)
    for list in user:
        if not working_list in connections:
            connections[working_list] = dict()
        if not list in connections[working_list]:
            connections[working_list][list] = 0
        connections[working_list][list] += 1
    crawl_list(user)

f = open(INFILE)
lines = f.read().split("\n")
f.close()

users = dict()
lists = dict()
connections = dict()
working_list = ''
for line in lines:
    line=line.strip()
    if line.isdigit():
        lists[working_list].append(line)
    else:
        working_list = line[:-1]
        lists[working_list] = []
for working_list in lists:
    if len(lists[working_list]) < MIN_CONS:
        continue
    if working_list[:5] == 'class':
        continue
    for user in lists[working_list]:
        if not user in users:
            users[user] = []
        users[user].append(working_list)
for user in users:
    crawl_list(users[user])

lists = dict()
nodes = []
links = []
for outer in connections:
    for inner in connections[outer]:
        if(connections[outer][inner] < MIN_CONS):
            continue
        if re.search(r'[20|\-]\d\d', outer) and re.search(r'[20|\-]\d\d', inner):
            continue
        if re.match(r'[a-z]+-', outer) and re.match(r'[a-z]+-', inner) and re.match(r'[a-z]+-', outer).group(0) == re.match(r'[a-z]+-', inner).group(0):
            continue
        if not outer in lists:
            lists[outer] = len(lists)
            nodes.append({"name":outer,"group":random.randint(1,10)})
        if not inner in lists:
            lists[inner] = len(lists)
            nodes.append({"name":inner,"group":random.randint(1,10)})
        links.append({"source":lists[outer],"target":lists[inner],"value":connections[outer][inner]})

with open(OUTFILE, 'w') as f:
    f.write(json.dumps({'nodes':nodes, 'links':links}))
