#!/usr/bin/env python3
print("What is your name?")

name = input("> ")

print(f"Hello {name}!")
# print("Hello {}!".format(name))
# print("Hello {name}!".format(name = name))
# print("Hello %s!" % (name))

# from string import Template
# print(Template("Hello $name!").substitute(name = name))