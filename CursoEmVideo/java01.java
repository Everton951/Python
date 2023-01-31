
package relembrando;

import java.util.Calendar;
import java.util.Scanner;

public class Relembrando {        

    public static void main(String[] args) { 
        
        
        int n[] = {3, 2, 4, 5, 7, 6, 8};
        
        for(int i = 0; i < n.length; i++) {
            System.out.print(n[i] + "  ");
        }
        System.out.println("\nTotal de números: " + n.length);
        
        for(int a = 0; a < n.length; a++) {
            System.out.println("Na posição " + (a + 1) + " temos o valor " + n[a]);
        }
    }
    
}
