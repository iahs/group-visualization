#!/bin/bash/python

import subprocess as s
import os
import sys

list_names_file = "lst"
output = "lists"
out_file = open(output, "w")

user_dict = dict()
list_dict = dict()

def load_lists(lists_file):
  """
  Opens the file that contains the names of the lists
  """
  f = open(lists_file, "rb")
  lists = f.read().split("\n")
  f.close()
  map(insert_into_list_dict, lists)

def insert_into_list_dict(list_name):
  list_dict[list_name] = []

def get_user_list(list_name):
  os.system("list_members " + list_name + " > " + list_name)
  if not os.path.isfile(list_name):
    print "exiting"
    sys.exit(2)
  f = open(list_name)
  users = f.read().split("\n")
  f.close()
  os.remove(list_name)
  return set(users)

def total_users():
  return len(dict)

def get_id_from_user(user):
  if user in user_dict :
    return user_dict[user]
  else :
    user_dict[user] = len(user_dict)
    return len(user_dict) - 1

load_lists(list_names_file)

for list in list_dict:
  if len(list) == 0: 
    continue
  print list
  out_file.write(list + ":\n")
  for user in get_user_list(list):
    out_file.write("  " + str(get_id_from_user(user)) + "\n")

out_file.close()
