#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except Exception as e:
    my_list = []
my_list = my_list + sys.argv[1:]
save_to_json_file(my_list, filename)
