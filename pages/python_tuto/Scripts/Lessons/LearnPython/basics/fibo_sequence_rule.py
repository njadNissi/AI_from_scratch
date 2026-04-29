def fibonacci(n):
  """
  This function calculates the nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def sequence_sum(n):
  """
  This function calculates the sum of the first n terms of the sequence, handling division by zero.
  """
  total_sum = 0
  for i in range(1, n+1):
    numerator = fibonacci(i)
    # Check if denominator is zero before division
    if i == 1:
      denominator = 1  # Handle first term (2/1) specifically
    else:
      denominator = fibonacci(i-1)
    total_sum += numerator / denominator
  return total_sum

# Calculate the sum of the first 20 terms
sum_of_20_terms = sequence_sum(20)

print("The sum of the first 20 terms is:", sum_of_20_terms)

