#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;

int main(int argc, char** argv)
{
    plt::plot({1,3,2,4});
    plt::show();

    return 0;
}