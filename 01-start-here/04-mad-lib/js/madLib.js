import readline from 'readline/promises';
const scanner = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let story = "The brave [ADJECTIVE] [NOUN] decided to [VERB] across the [ADJECTIVE] [PLACE] to rescue the [ADJECTIVE] [NOUN] from the evil [OCCUPATION]. After [VERB ENDING IN -ING] through [NUMBER] [PLURAL NOUN] and defeating a giant [ANIMAL], our hero finally [PAST TENSE VERB] and saved the day.";

for (const [original, name] of story.matchAll(/\[([A-Za-z\s\-]+)\]/g)) {
  const answer = await scanner.question(`What is a good ${name}?\n`);
  story = story.replace(original, answer);
}

console.log(story);