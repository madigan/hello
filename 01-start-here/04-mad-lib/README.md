---
tags: stdin, stdout, regex
---

# mad-lib

Collect words from the user and return a goofy sentence.

## Given

```shell
./quiz.rb
```

## Expect

```shell
What is a good ADJECTIVE?
> slimy
What is a good NOUN?
> pig
What is a good VERB?
> plod
What is your favorite NUMBER?
> 42
What is a good participle (-ING word)?
> LARPing
What is your favorite ANIMAL?
> koala
What is a good PLURAL NOUN?
> squeegees
The brave slimy pig decided to plod across the...
```

## Prompt

```
"The brave [ADJECTIVE1] [NOUN1] decided to [VERB1] across the [ADJECTIVE2] [PLACE1] to rescue the [ADJECTIVE3] [NOUN1] from the evil [OCCUPATION1]. After [VERB ENDING IN -ING1] through [NUMBER1] [PLURAL NOUN1] and defeating a giant [ANIMAL1], our hero finally [PAST TENSE VERB1] and saved the day."
```

Each word the user needs to fill in is surrounded by square brackets.
