abc = gets.split(' ').map(&:to_i).sort!
hl = gets.split(' ').map(&:to_i).sort!

if abc[0] <= hl[0] && abc[1] <= hl[1]
  puts 'S'
else
  puts 'N'
end
