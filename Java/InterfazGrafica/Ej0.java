package InterfazGrafica;

import javax.swing.*;
import java.awt.event.*;;

public class Ej0 extends JFrame implements ActionListener{
    
    private JTextField textField;
    private JLabel label1;
    private JButton button;

    public Ej0(){
        setLayout(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        label1=new JLabel("Mensaje");
        label1.setBounds(15, 10, 100, 30);
        add(label1);

        textField=new JTextField();
        textField.setBounds(80, 16, 190, 20);
        add(textField);

        button=new JButton("Mostrar");
        button.setBounds(10, 60, 100, 30);
        add(button);
        button.addActionListener(this);


    }

    public void actionPerformed(ActionEvent e){
        if(e.getSource()==button){
            String cadena=textField.getText();
            JOptionPane.showMessageDialog(null, cadena);


        }

    }

    public static void main(String[] args) {
        
        Ej0 ej0=new Ej0();
        ej0.setBounds(0,0, 300 , 150);
        ej0.setVisible(true);
        ej0.setLocationRelativeTo(null);

    }


}
