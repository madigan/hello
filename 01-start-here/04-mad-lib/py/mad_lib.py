#!/usr/bin/env python3
import re

story = "The brave [ADJECTIVE] [NOUN] decided to [VERB] across the [ADJECTIVE] [PLACE] to rescue the [ADJECTIVE] [NOUN] from the evil [OCCUPATION]. After [VERB ENDING IN -ING] through [NUMBER] [PLURAL NOUN] and defeating a giant [ANIMAL], our hero finally [PAST TENSE VERB] and saved the day."

groups = re.findall(r'\[[A-Z\s\-]+\]', story)
for group in groups:
    print(f"What is a good {group[1:-1]}?")
    answer = input("> ")
    story = story.replace(group, answer, count = 1)

print(story)