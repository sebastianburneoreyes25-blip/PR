package ejerciciosInterfaces.formularioConPoo;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class Formulario {
       public static void main(String[] args) {
        JFrame ventana = new JFrame("Persona");
        ventana.setSize(300, 200);
        ventana.setLayout(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField txtNombre = new JTextField();
        txtNombre.setBounds(100, 20, 150, 25);
        ventana.add(txtNombre);

        JLabel lblNombre = new JLabel("Nombre:");
        lblNombre.setBounds(30, 20, 150, 25);
        ventana.add(lblNombre);

        JTextField txtEdad = new JTextField();
        txtEdad.setBounds(100, 60, 150, 25);
        ventana.add(txtEdad);

        JLabel lblEdad = new JLabel("Edad:");
        lblEdad.setBounds(50, 60, 150, 25);
        ventana.add(lblEdad);

        JButton btn = new JButton("Crear persona");
        btn.setBounds(80, 100, 140, 30);
        ventana.add(btn);

        btn.addActionListener(e -> {
            try {
                String nombre = txtNombre.getText();
                String edadStr = txtEdad.getText();

                if (nombre.isEmpty())
                    throw new Exception("El nombre no puede estar vacío");

                if (!nombre.matches("[a-zA-Z ]+"))
                    throw new Exception("El nombre solo debe contener letras");

                int edad = Integer.parseInt(edadStr);

                if (edad <= 0)
                    throw new Exception("La edad debe ser mayor que 0");

                Persona p = new Persona(nombre, edad);

                JOptionPane.showMessageDialog(null,
                        "Nombre: " + p.getNombre() +
                        "\nEdad: " + p.getEdad());

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(null,
                        "La edad debe ser un número");
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(null, ex.getMessage());
            }
        });

        ventana.setVisible(true);
    }
}
