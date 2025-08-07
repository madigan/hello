#!/usr/bin/env ruby

template = "The brave [ADJECTIVE] [NOUN] decided to [VERB] across the [ADJECTIVE] [PLACE] to rescue the [ADJECTIVE] [NOUN] from the evil [OCCUPATION]. After [VERB ENDING IN -ING] through [NUMBER] [PLURAL NOUN] and defeating a giant [ANIMAL], our hero finally [PAST TENSE VERB] and saved the day."

template.scan(/\[[A-Z\s\-]+\]/).each do |item|
    puts "What is a good #{item.slice(1...-1)}?"
    print "> "
    answer = gets.strip
    template.sub!(item, answer)
end
puts template
