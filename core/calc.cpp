#include "calc.hpp"

double dist(double a[], double b[], int len) {
    double total = 0;
    for(int i=0; i<len; i++) {
        double tmp = a[i] - b[i];
        tmp *= tmp;
        total += tmp;
    }
    return sqrt(total);
}
double * dist_batch(double a[], double b[], const int dim, const int total_size) {
    const int num_coords = total_size / dim;
    double *distances = new double[num_coords];
    for(int i=0; i<num_coords; i++) {
        double *a_coord = new double[dim];
        double *b_coord = new double[dim];
        for(int j=0; j<dim; j++) {
            a_coord[j] = a[i * dim + j];
            b_coord[j] = b[i * dim + j];
        }
        distances[i] = dist(a_coord, b_coord, dim);
    }
    return distances;
}
int * neighboring_points(double coords[], int dim) {
    int i = (int)(pow(2, dim) - 1);
    int *placeholders = new int[dim];
    int *int_pos = new int[dim];
    int *signs = new int[dim];

    int *points = new int[dim * (i+1)];

    for(int a=0; a<dim; a++) {
        int_pos[a] = (int)coords[a];
        placeholders[a] = pow(2, a);
        signs[a] = 0;
        if(int_pos[a] < 0) signs[a] = -1;
        else if(int_pos[a] > 0) signs[a] = 1;
    }
    for(int a=0; a<i+1; a++) {
        int *index = new int[dim];

        for(int digit=0; digit<dim; digit++) {
            points[a * dim + digit] = int_pos[digit] + ((a & placeholders[digit]) >> digit) * signs[digit];
        }
    }
    return points;
}
