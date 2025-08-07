#!/usr/bin/env ruby
puts "What is your name?"
print "> "        # We don't want the automatic new line
name = gets.strip # gets includes the return character
puts "Hello #{name}!"