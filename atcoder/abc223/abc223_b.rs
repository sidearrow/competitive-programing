use std::io;

fn main() {
  let stdin = io::stdin();
  let mut s = String::new();
  let _ = stdin.read_line(&mut s);
  s = s.trim().to_string();

  let mut mn = s.clone();
  let mut mx = s.clone();

  for _ in 0..s.len() {
    let c = s.remove(0);
    s.push(c);
    if s < mn {
      mn = s.clone();
    }
    if s > mx {
      mx = s.clone();
    }
  }

  println!("{}", mn);
  println!("{}", mx);
}