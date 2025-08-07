use std::io::{self, Write};

fn main() {
    println!("What is your name?");
    print!("> ");
    io::stdout().flush().unwrap();

    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");
    
    println!("Hello {}!", name.trim());
}
