#define _USE_MATH_DEFINES // for C++
#include <cmath>
#include "matplotlibcppModified.h"
#include <iostream>

namespace plt = matplotlibcpp;

int main() 
{    
    std::vector<double> t(1000);
    std::vector<double> x(t.size());

    for(size_t i = 0; i < t.size(); i++) {
        t[i] = i / 100.0;
        x[i] = sin(2.0 * M_PI * 1.0 * t[i]);
    }
    {
        std::cout << "haha 1\n";
        plt::xkcd();
        std::cout << "haha 2\n";
        plt::plot(t, x);
        std::cout << "plt::plot\n";
        plt::title("AN ORDINARY SIN WAVE");
        std::cout << "haha 3\n";
        plt::save("xkcd.png");
        std::cout << "haha 4\n";
    }

    return 0;
}