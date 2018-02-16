import java.util.Scanner;

public class Aoj0004
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            double[] a = new double[6];
            for (int i = 0; i < 6; i++) {
                a[i] = sc.nextInt();
            }
            double x = ((a[2] * a[4] - a[5] * a[1]) / (a[0] * a[4] - a[3] * a[1]));
            double y = (a[2] - a[0] * x) / a[1];
            x = (x == -0) ? 0 : x;
            y = (y == -0) ? 0 : y;
            System.out.printf("%.3f %.3f\n", x, y);
        }
    }
}