#include "matplotlibcppModified.h"

namespace plt = matplotlibcpp;

int main() 
{
    //Define Data
    std::vector<double> x{ 0, 1, 2, 3, 4, 5 };
    std::vector<double> y{1.5, 2, 3.6, 14, 2.5, 3.9};
    //Plot 
    plt::plot(x, y);

    //Save as pdf
    plt::savefig( "mypic.pdf" );

    //Show image
    //plt::show();

    return 0;
}