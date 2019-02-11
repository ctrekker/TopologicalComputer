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
