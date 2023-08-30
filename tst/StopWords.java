//stop words

import java.util.Scanner;

class StopWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    
        String[] a = sc.nextLine().split(" ");
        String[] b = sc.nextLine().split(" ");
        String printavel = "";
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b.length; j++) {
                if (a[i].equals(b[j])) {
                    a[i] = "";
                }
            }
        }
        for (String palavra : a) {
            if (!palavra.trim().isEmpty()) {
                printavel += palavra + " ";
            }
        }
        System.out.println(printavel.trim());
    }
}