package ejerciciosInterfaces.ejercicio3;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

public class Ejercicio3 {
     public static void main(String[] args) {
        JFrame ventana = new JFrame("Áreas");
        ventana.setSize(350, 250);
        ventana.setLayout(null);

        JRadioButton rbRect = new JRadioButton("Rectángulo");
        rbRect.setBounds(20, 20, 120, 25);

        JRadioButton rbCirc = new JRadioButton("Círculo");
        rbCirc.setBounds(150, 20, 120, 25);

        ButtonGroup grupo = new ButtonGroup();
        grupo.add(rbRect);
        grupo.add(rbCirc);

        JTextField txt1 = new JTextField();
        txt1.setBounds(20, 60, 120, 25);

        JTextField txt2 = new JTextField();
        txt2.setBounds(150, 60, 120, 25);

        JButton btn = new JButton("Calcular área");
        btn.setBounds(90, 110, 150, 30);

        ventana.add(rbRect);
        ventana.add(rbCirc);
        ventana.add(txt1);
        ventana.add(txt2);
        ventana.add(btn);

        btn.addActionListener(e -> {
            try {
                Forma forma;

                if (rbRect.isSelected()) {
                    double base = Double.parseDouble(txt1.getText());
                    double altura = Double.parseDouble(txt2.getText());

                    if (base <= 0 || altura <= 0)
                        throw new Exception("Valores inválidos");

                    forma = new Rectangulo(base, altura);

                } else if (rbCirc.isSelected()) {
                    double radio = Double.parseDouble(txt1.getText());

                    if (radio <= 0)
                        throw new Exception("Radio inválido");

                    forma = new Circulo(radio);

                } else {
                    throw new Exception("Seleccione una figura");
                }

                double area = forma.calcularArea();

                JOptionPane.showMessageDialog(null,
                        "Área: " + area);

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(null,
                        "Ingrese valores numéricos");
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(null, ex.getMessage());
            }
        });

        ventana.setVisible(true);
    }
}
