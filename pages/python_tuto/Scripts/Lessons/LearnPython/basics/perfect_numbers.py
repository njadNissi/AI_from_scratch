def is_perfect(num):
  """
  This function checks if a number is a perfect number and returns a list of its factors.
  """
  if num <= 1:
    return False
  factors = [1]  # Initialize factors list with 1 (always a factor)
  sum_of_factors = 1
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      factors.append(i)
      sum_of_factors += i
      if i * i != num:  # Add the pair only once if it's a perfect square
        factors.append(num // i)
        sum_of_factors += num // i
  return factors if sum_of_factors == num else False

# Find all perfect numbers within 1000
perfect_numbers = []
for num in range(2, 1001):
  factors = is_perfect(num)
  if factors:
    perfect_numbers.append((num, factors, sum(factors)))

# Print the results in desired format
print("Perfect numbers between 1 and 1000:")
for num, factors, total in perfect_numbers:
  print(f"Factors: {factors}, Sum: {total} = Perfect Number: {num}")

