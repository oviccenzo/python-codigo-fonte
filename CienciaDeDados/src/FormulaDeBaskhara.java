import java.util.Scanner;

public class FormulaDeBaskhara{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite os tres coeficiente de a , b e c(axˆ2 + bx + c): ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        double delta = (b * b) - 4 * a * c;

        if(delta > 0){
            double x1 = (-b + Math.sqrt(delta)) / (2.0 * a);
            double x2 = (-b - Math.sqrt(delta)) / (2.0 * a);
            System.out.printf("As raizes da equação é x1 = %.4f e x2 = %.4f\n",x1,x2);
        } else {
            System.out.println("As raizes da equação de 2 grau não tem raízes exata");
        }
    }
}