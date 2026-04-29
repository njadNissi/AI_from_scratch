// mylib.cpp
#include <iostream>

// --- Boilerplate for cross-platform export ---
#ifdef _WIN32
    #define MYLIB_EXPORT __declspec(dllexport)
#else
    #define MYLIB_EXPORT
#endif


// ---------------------------------------------


extern "C" {

    // A simple function that adds two integers and prints from C++
    // The MYLIB_EXPORT macro makes it visible outside the DLL/SO
    MYLIB_EXPORT int add_numbers_cpp(int a, int b) {
        std::cout << "  [C++] Inside C++ code. Receiving " << a << " and " << b << std::endl;
        int result = a + b;
        return result;
    }

}