package com.burnscoding.tc;

import java.awt.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.Timer;
import javax.swing.*;

public class Gradient2DTerrain extends JFrame {
    public static void main(String[] args) throws Exception {
        Gradient2DTerrain g = new Gradient2DTerrain(args[0], args[1]);
    }

    private RenderCanvas canvas;
    private static int w = 640;
    private static int h = 640;

    private double scaleX = 2;
    private double scaleY = 0.5;

    public Gradient2DTerrain(String terrainFilename, String signalsFilename) throws FileNotFoundException {
        Scanner terrainFileReader = new Scanner(new File(terrainFilename));
        Scanner signalsFileReader = new Scanner(new File(signalsFilename));
        // Read header
        String line = terrainFileReader.nextLine();
        w = (int)(line.split(",").length * scaleX);

        setTitle("Gradient 2D Terrain Renderer");
        setSize(w, h);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        addWindowStateListener(e -> {
            Dimension d = e.getWindow().getSize();
            w = d.width;
            h = d.height;
        });
        canvas = new RenderCanvas(terrainFileReader, signalsFileReader);
        add(canvas);
        setVisible(true);
    }

    private class RenderCanvas extends Component {
        private Timer animationTimer;
        private Scanner terrainIn;
        private Scanner signalsIn;
        private int frame = 0;
        private int speed = 1;

        public RenderCanvas(Scanner terrainIn, Scanner signalsIn) {
            this.terrainIn = terrainIn;
            this.signalsIn = signalsIn;
            animationTimer = new Timer();
            animationTimer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    repaint();
                }
            }, 0, 1000/60);
        }

        int[] displayLine;
        int[] xCoords;
        int[] signalsPositions;

        @Override
        public void paint(Graphics g) {
            Graphics2D g2 = (Graphics2D) g;

            int dropped = speed - 1;
            while(terrainIn.hasNextLine() && dropped != 0) {
                terrainIn.nextLine();
                signalsIn.nextLine();
                dropped--;
            }
            if(terrainIn.hasNextLine()) {
                String[] currentTerrainLine = terrainIn.nextLine().split(",");
                String[] currentSignalsLine = signalsIn.nextLine().split(",");
                displayLine = new int[currentTerrainLine.length];
                signalsPositions = new int[currentSignalsLine.length];
                for (int i = 0; i < currentTerrainLine.length; i++) {
                    displayLine[i] = (int) (h / 2.0 - Double.parseDouble(currentTerrainLine[i]) * scaleY);
                }
                for(int i=0; i<currentSignalsLine.length; i++) {
                    try {
                        if (i % 2 == 1) {
                            // Y coords
                            signalsPositions[i] = (int) (h / 2.0 - Double.parseDouble(currentSignalsLine[i]) * scaleY);
                        } else {
                            // X coords
                            signalsPositions[i] = (int) (Double.parseDouble(currentSignalsLine[i]) * scaleX);
                        }
                    } catch(NumberFormatException e) {
                        signalsPositions[i] = 0;
                    }
                }

                xCoords = new int[currentTerrainLine.length];
                for (int i = 0; i < currentTerrainLine.length; i++) {
                    xCoords[i] = (int)(i*scaleX);
                }
                frame+=speed;
            }

            g2.setStroke(new BasicStroke(2));
            g2.setColor(Color.BLACK);
            g2.drawPolyline(xCoords, displayLine, displayLine.length);

            int arcSize = 10;
            g2.setStroke(new BasicStroke(1));
            for(int i=0; i<signalsPositions.length; i+=2) {
                g2.drawArc((int)(signalsPositions[i] - arcSize / 2.0), (int)(signalsPositions[i+1] - arcSize / 2.0), arcSize, arcSize, 0, 360);
            }

            g2.drawString((frame-1)+"", 0, 15);
        }
    }
}
