use rand::Rng;
use std::cmp::Ordering;
use std::io::{self, Write};

fn main() {
    let answer = rand::rng().random_range(1..=10);

    println!("🔮 Can you guess the magic number?");

    loop {
        let mut guess = String::new();
        print!("> ");
        io::stdout().flush().unwrap();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read input.");

        let guess: i32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("🔮 '{}' is not a number.", guess.trim());
                continue;
            },
        };

        match guess.cmp(&answer) {
            Ordering::Equal => {
                println!("🔮 You got it!");
                break;
            }
            Ordering::Greater => println!("🔮 Too high!"),
            Ordering::Less => println!("🔮 Too low!"),
        }
    }
}
