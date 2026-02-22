import java.util.Scanner;

public class Baskhara {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Os coeficiente de a b e c da equação de baskhara(axˆ2 + bx + c)");

        System.out.println("O coeficiente a: ");
        double a = scanner.nextDouble();

        System.out.println("O coeficiente b: ");
        double b = scanner.nextDouble();

        System.out.println("O coeficiente c: ");
        double c = scanner.nextDouble();

        double delta = Math.pow(b, 2.0) - 4 * a * c;

        if (delta > 0 ){
            double x1 = (-b + Math.sqrt(delta)) / (2.0 * a);
            double x2 = (-b - Math.sqrt(delta)) / (2.0 * a);
            System.out.printf("A raizes da equação é: x1 = %.2f e x2 = %.2f\n", x1,x2);
        } else{
            System.out.println("As raizes não tem equação reais");
        }
    }
}
