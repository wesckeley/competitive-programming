data = gets.split(' ').map(&:to_i)
data.sort!
puts data[1]
