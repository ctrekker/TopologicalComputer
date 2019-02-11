#include <iostream>
#include <chrono>
#include <sstream>
#include <math.h>

using namespace std;

namespace timer {
    chrono::time_point<chrono::high_resolution_clock> timer_started;
    void start() {
        timer_started=chrono::high_resolution_clock::now();
    }
    uint64_t stop(string str) {
        auto timer_stopped=chrono::high_resolution_clock::now();
        int64_t time = std::chrono::duration_cast<std::chrono::nanoseconds>(timer_stopped-timer_started).count();
        uint64_t millis_time = time / 1000000;
        string label = "ns";
        if(time>10000) {
            time/=1000;
            label="us";
        }
        if(time>10000) {
            time/=1000;
            label="ms";
        }
        if(time>10000) {
            time/=1000;
            label="s";

            if(time>120) {
                time/=60;
                label="m";
            }
            if(time>120) {
                time/=60;
                label="h";
            }
        }
        cout << str << " in " << time << label << endl;

        return millis_time;
    }
    uint64_t getTimeMillis() {
        return std::chrono::duration_cast<std::chrono::milliseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count();
    }
}

/*
A c++ version of algorithm #1 within fastest_distance_formula.py.
The c++ version is about 250 times faster than the python version
*/
void test_distance_formula() {
    const int quantity = 1000000;
    const int dim = 3;
    int** u_vectors = new int*[quantity];
    int** v_vectors = new int*[quantity];
    double* results = new double[quantity];
    cout << "Constructing " << quantity << " random vectors..." << endl;
    for(int i=0; i<quantity; i++) {
        u_vectors[i] = new int[dim];
        v_vectors[i] = new int[dim];
        for(int j=0; j<dim; j++) {
            u_vectors[i][j] = rand() % 200 - 100;
            v_vectors[i][j] = rand() % 200 - 100;
        }
    }

    cout << "Executing distance formula" << endl;
    timer::start();
    for(int i=0; i<quantity; i++) {
        double total = 0;
        for(int j=0; j<dim; j++) {
            int v = u_vectors[i][j] - v_vectors[i][j];
            v *= v;
            total += v;
        }
        results[i] = sqrt(total);
    }
    timer::stop("Calculated distances");

    cout << "Example:" << endl;
    cout << "\tVector<";
    for(int i=0; i<dim; i++) {
        cout << u_vectors[0][i] << ",";
    }
    cout << "> + Vector<";
    for(int i=0; i<dim; i++) {
        cout << v_vectors[0][i] << ",";
    }
    cout << ">";
    cout << " = " << results[0] << endl;}
int main()
{
    test_distance_formula();

    return 0;
}
