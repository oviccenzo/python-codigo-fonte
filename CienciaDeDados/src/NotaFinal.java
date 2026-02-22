import java.util.Scanner;
import java.util.Locale;

public class NotaFinal {

    public static void main(String[] args){

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe a primeira nota do bimestre: ");
        double PrimeiraNota = sc.nextDouble();

        System.out.println("Informe a segunda nota do bimestre: ");
        double SegundaNota = sc.nextDouble();

        double NotaFinal = PrimeiraNota - SegundaNota;

        System.out.printf("A nota final do aluno é: %.2f %n", NotaFinal);

        if(NotaFinal < 60){
            System.out.print("Reprovado");
        } else{
            System.out.print("Aprovado");
        }
    }
}

class notaFinal{

    public static void main(String[] args){

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe a nota do Primeiro Semestre do aluno: ");
        double PrimeiraNota = sc.nextDouble();

        System.out.println("informe a nota do Segundo Semestre do aluno: ");
        double SegundaNota = sc.nextDouble();

        double NotaFinal = PrimeiraNota + SegundaNota;

        System.out.printf("A nota final do aluno é: %.2f %n",NotaFinal);

        if(NotaFinal < 60){
            System.out.println("Reprovado");
        } else {
            System.out.println("Aprovado");
        }
    }
}