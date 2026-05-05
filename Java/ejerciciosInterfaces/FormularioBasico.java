package ejerciciosInterfaces;
 import javax.swing.*;
import java.awt.event.*;
public class FormularioBasico {


public class Ejercicio1 {
    public static void main(String[] args) {
        
    
        JFrame ventana = new JFrame("Formulario");
        ventana.setSize(300, 200);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setLayout(null);

        JLabel lblNombre = new JLabel("Nombre:");
        lblNombre.setBounds(20, 20, 80, 25);
        ventana.add(lblNombre);

        JTextField txtNombre = new JTextField();
        txtNombre.setBounds(100, 20, 150, 25);
        ventana.add(txtNombre);

        JLabel lblEdad = new JLabel("Edad:");
        lblEdad.setBounds(20, 60, 80, 25);
        ventana.add(lblEdad);

        JTextField txtEdad = new JTextField();
        txtEdad.setBounds(100, 60, 150, 25);
        ventana.add(txtEdad);

        JButton btnEnviar = new JButton("Enviar datos");
        btnEnviar.setBounds(80, 100, 130, 30);
        ventana.add(btnEnviar);

        btnEnviar.addActionListener(e -> {
            try {
                String nombre = txtNombre.getText();
                String edad = txtEdad.getText();

                if (nombre.isEmpty() || edad.isEmpty()) {
                    throw new Exception("Campos vacíos");
                }

                System.out.println("Nombre: " + nombre);
                System.out.println("Edad: " + edad);

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(null,
                        "Todos los campos son obligatorios");
            }
        });

        ventana.setVisible(true);
    }
}
}
