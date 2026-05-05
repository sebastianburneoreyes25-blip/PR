package ejerciciosInterfaces.dibujoBasico;

import javax.swing.*;
import java.awt.*;

public class Ejercicio4 extends JPanel {

    private String figura = "";

    public void setFigura(String figura) {
        this.figura = figura;
        repaint();
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        if (figura.equals("rect")) {
            g.drawRect(50, 50, 100, 60);
        } else if (figura.equals("circ")) {
            g.drawOval(50, 50, 100, 100);
        }
    }

    public static void main(String[] args) {
        JFrame ventana = new JFrame("Dibujo");
        ventana.setSize(300, 300);

        Ejercicio4 panel = new Ejercicio4();

        JButton btnRect = new JButton("Dibujar rectángulo");
        JButton btnCirc = new JButton("Dibujar círculo");

        btnRect.addActionListener(e -> panel.setFigura("rect"));
        btnCirc.addActionListener(e -> panel.setFigura("circ"));

        ventana.setLayout(new BorderLayout());
        JPanel botones = new JPanel();

        botones.add(btnRect);
        botones.add(btnCirc);

        ventana.add(panel, BorderLayout.CENTER);
        ventana.add(botones, BorderLayout.SOUTH);

        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setVisible(true);
    }
}