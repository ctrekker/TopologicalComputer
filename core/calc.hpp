#ifndef CALC_HPP
#define CALC_HPP

#include <stdio.h>
#include <math.h>
#include <cstdlib>

double dist(double a[], double b[], int len);
double * dist_batch(double a[], double b[], const int dim, const int total_size);

#endif // CALC_HPP
