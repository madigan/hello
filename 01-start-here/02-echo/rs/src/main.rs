use std::env;

// Note that collect needs "turbofish" (::<>) to clarify what type is collects to.
// If we didn't need spacing, we could have collected to a String.
fn main() { 
    println!("{}", env::args().skip(1).collect::<Vec<String>>().join(" "));
}
