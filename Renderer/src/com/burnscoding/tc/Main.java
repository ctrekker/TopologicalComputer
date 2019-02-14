package com.burnscoding.tc;

public class Main {
    public static void main(String[] args) throws Exception {
        String command = args[0];
        String[] new_args = new String[args.length-1];
        for(int i=0; i<new_args.length; i++) {
            new_args[i] = args[i+1];
        }
        switch(command.toLowerCase()) {
            case "list":
                System.out.println("Gradient2DTerrain, GradientFunction, Renderer");
                break;
            case "gradient2dterrain":
                Gradient2DTerrain.main(new_args);
                break;
            case "gradientfunction":
                GradientFunction.main(new_args);
                break;
            case "renderer":
                Renderer.main(new_args);
                break;
        }
    }
}
