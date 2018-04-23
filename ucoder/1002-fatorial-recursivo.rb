def factorial(value)
  if value == 1
    return 1
  else
    return value * factorial(value - 1)
  end
end

x = gets.to_i
puts factorial(x)
