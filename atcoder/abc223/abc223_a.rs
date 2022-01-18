use std::io;

fn main() {
    let mut s = String::new();
    let stdin = io::stdin();
    let _ = stdin.read_line(&mut s);
    let n: u32 = s.trim().parse().unwrap();
    println!("{}", if solve(n) { "Yes" } else { "No"});
}

fn solve(n: u32) -> bool {
    return n > 0 && n % 100 == 0;
}