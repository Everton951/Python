package relembrando;

import java.util.Scanner;

public class Relembrando {        

    public static void main(String[] args) {  
        
        Scanner tec = new Scanner(System.in);
        
        System.out.print("Digite o seu nome: ");
        String nome = tec.nextLine();
        
        System.out.printf("Digite a nota de %s: ", nome);
        float nota = tec.nextFloat();
        
        System.out.printf("Digite a idade de %s: ", nome);
        int idade = tec.nextInt();
        
        System.out.printf("Digite o salário de %s: ", nome);
        float sal = tec.nextFloat();
        
        System.out.printf("A nota de %s é %.1f", nome, nota);
        System.out.println("\nA idade de " + nome + " é " + idade + " anos.");
        System.out.println("O salário de " + nome + " é igual a " + sal + " reais.");
    }
    
}
