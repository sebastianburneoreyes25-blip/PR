package ejerciciosInterfaces.dibujoConEntrada;

import javax.swing.*;
import java.awt.*;

public class Ejercicio5 extends JPanel {

    private int size = 0;

    public void setSizeCuadrado(int size) {
        this.size = size;
        repaint();
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (size > 0) {
            g.drawRect(50, 50, size, size);
        }
    }

    public static void main(String[] args) {
        JFrame ventana = new JFrame("Cuadrado");
        ventana.setSize(300, 300);

        Ejercicio5 panel = new Ejercicio5();

        JTextField txt = new JTextField(10);
        JButton btn = new JButton("Dibujar cuadrado");

        btn.addActionListener(e -> {
            try {
                int valor = Integer.parseInt(txt.getText());

                if (valor <= 0)
                    throw new Exception("Debe ser mayor que 0");

                panel.setSizeCuadrado(valor);

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(null,
                        "Debe ser un número");
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(null, ex.getMessage());
            }
        });

        JPanel controles = new JPanel();
        controles.add(txt);
        controles.add(btn);

        ventana.setLayout(new BorderLayout());
        ventana.add(panel, BorderLayout.CENTER);
        ventana.add(controles, BorderLayout.SOUTH);

        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setVisible(true);
    }
}
