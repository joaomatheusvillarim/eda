//vetor circular
import java.util.Scanner;

class VetorCircular {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split(" ");
        int n = sc.nextInt();
        String printavel = "";
        for (int i = 0; i < n; i++) {
            printavel += a[i % a.length] + " ";
        }
        System.out.println(printavel.trim());
    }
}