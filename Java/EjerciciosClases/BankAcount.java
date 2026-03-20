package Java.EjerciciosClases;

public class BankAcount {
    
    float balance;

    public BankAcount(float balance){
        this.balance=balance;
    }

    public void deposit(float deposit){
        this.balance+=deposit;
        System.out.println("Se ha actualizado el balance");
    }

}
