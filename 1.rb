# 1a
def numeric?(lookAhead)
    lookAhead.match?(/[[:digit:]]/)
end

file = File.open("1.txt", "r")
totalFile = []
file.each_line do |line|
    totalLine = []
    line.each_char do |char|
        if numeric?(char)
            totalLine << char
        end
    end
    totalFile << totalLine.first + totalLine.last
end

sum = 0
for number in totalFile do
    sum += number.to_i
end
puts sum

