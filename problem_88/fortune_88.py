quotient, remainder = 0, 0
divisor, dividend = 13, 157

while dividend >= divisor:
  dividend -= divisor
  quotient += 1

remainder = dividend

print(f"quotient: {quotient}, remainder: {remainder}")
