%module calc

%{
#define SWIG_FILE_WITH_INIT
#include "calc.hpp"
%}

%include "carrays.i"
%array_class(int, intArray);
%array_class(double, doubleArray);

double dist(double a[], double b[], int len);
double * dist_batch(double a[], double b[], const int dim, const int total_size);
int * neighboring_points(double coords[], int dim);
