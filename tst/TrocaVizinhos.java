// troca vizinhos
import java.util.Scanner;
import java.util.Arrays;

class TrocaVizinhos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] a = sc.nextLine().split(" ");
        String dummy = "";
        for (int i = 0; i < a.length; i++) {
            if (i%2==0) {
                dummy = a[i];
            } else {
                a[i-1] = a[i];
                a[i] = dummy;
            }
        }
        System.out.println(Arrays.toString(a));
    }
}