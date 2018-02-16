import java.util.Scanner;

public class Aoj0002
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()) {
            int a = String.valueOf(sc.nextInt() + sc.nextInt()).length();
            System.out.println(a);
        }
    }
}