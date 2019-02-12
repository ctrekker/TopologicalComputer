#ifndef CALC_HPP
#define CALC_HPP

#include <stdio.h>
#include <math.h>
#include <cstdlib>
#include <cmath>

double dist(double a[], double b[], int len);
double * dist_batch(double a[], double b[], const int dim, const int total_size);
int * neighboring_points(double coords[], int dim);

#endif // CALC_HPP
