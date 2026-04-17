public class Account {
    float saldo;

    public void deposit(float deposito){
        this.saldo+=deposito;
    }

    public void withDraw(float retirar){
        this.saldo-=retirar;
    }

    public class SavingAcoount extends Account{

        public void addInterst(){
            this.saldo+=saldo*.05;
        }
    }
}
