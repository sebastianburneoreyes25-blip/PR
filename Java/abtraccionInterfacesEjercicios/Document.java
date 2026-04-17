package abtraccionInterfacesEjercicios;



public abstract class Document {
    
    abstract void print();

    public static class  PDFDocument extends Document {

    
        @Override
        void print(){
            System.out.println("Imprime PDF");
        }
    }
    public static class  WordDocument extends Document {

    
        @Override
        void print(){
            System.out.println("Imprime WordDocument");
        }
    }
    public static void main(String[] args) {
        PDFDocument p=new PDFDocument();
        WordDocument w=new WordDocument();
        p.print();
        w.print();
    }

}
