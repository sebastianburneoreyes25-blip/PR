


public  class Device {
    
    public Device(){
        System.out.println("Device created");

    }


    public  static class Phone extends Device{
        
        public Phone(){
            
            System.out.println("Phone is ready");
        }
    }

    public static void main(String[] args) {
        Phone phone=new Phone();
        
    }
    
}
