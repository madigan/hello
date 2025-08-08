---
tags:
  - stdin
  - stdout
  - rand
  - switch/case
  - parseInt
  - error handling
---

# mind reader

🔮 Can you guess the magic number?

- [ ] Randomly choose a number in the [1,10] range.
- [ ] Prompt the user to guess: "🔮 Can you guess the magic number?"
- [ ] Capture the input from the user
  - [ ] If the input is not a number, state: "🔮 'INPUT' is not a number."
  - [ ] If the guess is too low, say "🔮 Too low!"
  - [ ] If the guess is too high, say "🔮 Too high!"
  - [ ] If the guess is correct, say "🔮 You got it!" and end the program.

```zsh
./mind_reader
🔮 Can you guess the magic number?
> 10
🔮 Too high!
> 3
🔮 Too low!
> foo
🔮 'foo' is not a number.
> 4
🔮 You got it!
```
