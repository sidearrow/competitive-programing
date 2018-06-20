import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    while(sc.hasNext()) {
      int a = String.valueOf(sc.nextInt() + sc.nextInt()).length();
      System.out.println(a);
    }
  }
