n = gets.to_i
data =  gets.split(' ').map(&:to_i)

max_local = 0
max_global = 0
j = 0

for i in 0..n-1

  if data[i] == data[j]
    max_local += 1
  else
    j = i
    max_local = 1
  end

  if max_local > max_global
    max_global = max_local
  end

end

puts max_global
