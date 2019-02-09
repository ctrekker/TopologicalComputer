package com.burnscoding.tc;

import java.awt.*;
import java.awt.event.WindowEvent;
import java.awt.event.WindowStateListener;
import java.util.*;
import java.util.Timer;
import javax.swing.*;

public class Renderer extends JFrame {
    public static void main(String[] args) {
        Renderer r = new Renderer();
    }

    private RenderCanvas canvas;
    private static int w = 640;
    private static int h = 640;

    public Renderer() {
        setTitle("Topological Computer");
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

        double step = 0.01;
        double[] points = new double[640];
        double ballX = 640;
        double ballY = 0;

        double d = 0.001;

        Vector2D gravity = new Vector2D(0, -1);
        Vector2D momentum = new Vector2D(0, 0);
        double friction = 1.025;

        public RenderCanvas() {
            animationTimer = new Timer();
            animationTimer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    repaint();
                }
            }, 0, 1000/60);

            // Init hill terrain
            for(int x=0; x<points.length; x++) {
                points[x] = gradientFunction(x);
            }
        }

        private double gradientFunction(double x) {
//            Cosine
//            return Math.cos(x*step)*(h/4.0);

//            Parabola
//            return (1.0/640.0)*Math.pow(x-320.0, 2)-150;

//            Polynomial
//            double o = 3.9;
//            double z = 60;
//            return ((-z)*Math.pow((x/z)-o, 4)
//                    +2*z*Math.pow((x/z)-o, 3)
//                    +15*z*Math.pow((x/z)-o, 2)
//            )/20.0;

//            Sine and hill
            return 10*Math.sin(x/16.0)+Math.pow(2, 0.015*x);
        }

        @Override
        public void paint(Graphics g) {
            Graphics2D g2 = (Graphics2D) g;

            int[] xPoints = new int[points.length];
            int[] yPoints = new int[points.length];

            for(int i=0; i<xPoints.length; i++) {
                xPoints[i] = i;
                yPoints[i] = (int)(h - h/3.0 - points[i]);
            }

            g2.drawPolyline(xPoints, yPoints, xPoints.length);
            g2.fillArc((int)ballX - 10, (int)(h - h/3.0 - ballY) - 10, 20, 20, 0, 360);

            Vector2D result = gravity.add(momentum);
            Vector2D slope = new Vector2D((ballX+d)-(ballX-d), gradientFunction(ballX+d)-gradientFunction(ballX-d));

            momentum = result.projectOnto(slope).divide(friction);
            ballX += momentum.x;
            ballY = gradientFunction(ballX);
        }
    }
}
