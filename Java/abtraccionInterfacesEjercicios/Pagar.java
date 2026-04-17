package abtraccionInterfacesEjercicios;


public class Pagar {

    public interface Payable {
        void pay();
        
    }
    
    public static class  Invoice implements Payable {
        
        @Override
        public void pay() {
           System.out.println("FACTURA");
            
        }
        
    }
    public static class  EmployeePay implements Payable {
    
        @Override
        public void pay() {
            System.out.println("Employee Paying");
        }
        
    }

    public static void main(String[] args) {
        EmployeePay ep=new EmployeePay();
        Invoice i=new Invoice();
        ep.pay();
        i.pay();

    }
}
