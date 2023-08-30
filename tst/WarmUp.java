//warm up
import java.util.Scanner;

class WarmUp {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] a = sc.nextLine().split(" ");
        for (int i = 0; i < a.length; i ++) {
            int x = Integer.parseInt(a[i]) * n;
            a[i] = Integer.toString(x);
        }
        String printavel = "";
        for (String i : a) {
            printavel += i + " ";
        }
        System.out.println(printavel.trim() + "\n");
    }

}