// Joel Guanoluisa
//UEA
import java.util.Scanner;

public class matrices {
    public static void main(String[] args) {
        
        int[][] asientos = new int[3][4];
        Scanner teclado = new Scanner(System.in);

        // 2. Pedir al usuario la fila y la columna
        System.out.print("Ingrese fila (0 a 2): ");
        int f = teclado.nextInt();

        System.out.print("Ingrese columna (0 a 3): ");
        int c = teclado.nextInt();

        
        if (f >= 0 && f <= 2 && c >= 0 && c <= 3) {
            
            asientos[f][c] = 1;
            System.out.println("\n¡Asiento reservado con éxito!");
        } else {
            System.out.println("\nError: Índices fuera de rango (Fila 0-2, Columna 0-3).");
        }

        
        System.out.println("\nEstado de la sala:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print(asientos[i][j] + " ");
            }
            System.out.println();
        }

        teclado.close();
    }
}
