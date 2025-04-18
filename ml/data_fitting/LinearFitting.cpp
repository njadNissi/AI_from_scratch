#include <iostream>
#include <tuple>
#include <vector>

// LinearFitting algorithm
std::tuple<double, double> linearFit(const std::vector<double> &x,
                                     const std::vector<double> &y) {
  if (x.size() != y.size() || x.empty()) {
    throw std::invalid_argument(
        "Input vectors must be of the same non-zero size.");
  }
  size_t N = x.size();
  double sumX = 0.0, sumY = 0.0, sumXY = 0.0, sumX2 = 0.0;

  // Calculate: sum(X), sum(Y), sum(X*Y), sum(X^2)
  for (size_t i = 0; i < N; ++i) {
    sumX += x[i];
    sumY += y[i];
    sumXY += x[i] * y[i];
    sumX2 += x[i] * x[i];
  }

  // Calculate: Slope (m) and Bias (b)
  double m = (N * sumXY - sumX * sumY) / (N * sumX2 - sumX * sumX + 1e-5);
  double b = (sumY - m * sumX) / N;

  return std::make_tuple(m, b);
}

int main() {

  // Sample data 
  std::vector<double> x = {1, 2, 3, 4, 5};
  std::vector<double> y = {2, 4, 5, 4, 5};

  try {
    // Apply linear fitting
    auto [m, b] = linearFit(x, y);
    // Show Result
    std::cout << "The fitting eequation: y = " << m << " * x + " << b << std::endl;
    // Predicted Value        
    double newX = 6;
    double predictedY = m * newX + b;
    std::cout << "For x = " << newX << ", predicted y = " << predictedY
              << std::endl;
  } catch (const std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
  }

  return 0;
}