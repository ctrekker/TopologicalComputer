package com.burnscoding.tc;

import java.awt.*;
import java.awt.event.WindowEvent;
import java.awt.event.WindowStateListener;
import java.util.*;
import java.util.Timer;
import javax.swing.*;

public class GradientFunction extends JFrame {
    public static void main(String[] args) {
        GradientFunction gradientFunction = new GradientFunction();
    }

    private RenderCanvas canvas;
    private static int w = 640;
    private static int h = 640;

    public GradientFunction() {
        setTitle("Gradient Function");
        setSize(w, h);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        addWindowStateListener(e -> {
            Dimension d = e.getWindow().getSize();
            w = d.width;
            h = d.height;
        });
        canvas = new RenderCanvas();
        add(canvas);
        setVisible(true);
    }

    private class RenderCanvas extends Component {
        private Timer animationTimer;
        private int[][] points = {
                { 10, 2 },
                { 20, 3 }
        };

        public RenderCanvas() {
            animationTimer = new Timer();
//            animationTimer.scheduleAtFixedRate(new TimerTask() {
//                @Override
//                public void run() {
//                    repaint();
//                }
//            }, 0, 1000/60);
        }

        public double gf(double xp, double yp) {
            double yIntercept = points[0][0];
            double slopeX = points[1][0] - points[0][0];
            double slopeY = points[0][1] - points[0][0];
            return xp*slopeX + yp*slopeY + yIntercept;
        }

        double map(double x, double in_min, double in_max, double out_min, double out_max)
        {
            return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
        }

        int inset = 50;
        int startX = inset;
        int startY = inset;
        int endX = w - inset * 2;
        int endY = h - inset * 2;

        @Override
        public void paint(Graphics g) {
            Graphics2D g2 = (Graphics2D) g;

            g2.setStroke(new BasicStroke(2));
            g2.setColor(Color.BLACK);
            g2.drawRect(startX, startY, endX - startX, endY - startY);

            double min = 3;
            double max = 1;

            for(double x = 0; x < 1.0; x += 1.0 / (endX - startX)) {
                for (double y = 0; y < 1.0; y += 1.0 / (endY - startY)) {
                    double z = gf(x, y);
                    if (z < min) {
                        min = z;
                    }
                    if (z > max) {
                        max = z;
                    }
                }
            }

            int xCoord = startX;
            int yCoord = startY;
            for(double x = 0; x < 1.0; x += 1.0 / (endX - startX)) {
                for(double y = 0; y < 1.0; y += 1.0 / (endY - startY)) {
                    double z = gf(x, y);
                    z = map(z, min, max, 0, 255);

                    if(z < 0 || z > 255) {
                        g2.setPaint(new Color(0, 0, 255));
                    }
                    else {
                        g2.setPaint(new Color((int)z, (int)z, (int)z));
                    }
                    g2.fillRect(xCoord, yCoord, 1, 1);
                    yCoord++;
                }
                xCoord++;
                yCoord = startY;
            }
            System.out.println("Min:"+min);
            System.out.println("Max:"+max);
        }
    }
}
