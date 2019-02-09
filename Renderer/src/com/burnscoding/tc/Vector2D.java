package com.burnscoding.tc;

public class Vector2D {
    double x = 0;
    double y = 0;
    public Vector2D() { }
    public Vector2D(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public Vector2D add(Vector2D other) {
        return new Vector2D(this.x + other.x, this.y + other.y);
    }
    public Vector2D subtract(Vector2D other) {
        return new Vector2D(this.x - other.x, this.y - other.y);
    }
    public double multiply(Vector2D other) {
        return this.x * other.x + this.y * other.y;
    }
    public Vector2D multiply(double d) {
        return new Vector2D(x*d, y*d);
    }
    public Vector2D divide(double d) {
        return new Vector2D(x/d, y/d);
    }
    public double magnitude() {
        return Math.sqrt(x*x + y*y);
    }
    public double angle() {
        return Math.atan(x / y);
    }
    public Vector2D projectOnto(Vector2D v) {
        return v.multiply(this.multiply(v)/Math.pow(v.magnitude(), 2));
    }

    @Override
    public String toString() {
        return "Vector2D<"+x+","+y+">";
    }
}
