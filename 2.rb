file = File.open("2.txt", "r")
file.each_line do |line|
    game = line.split(':')[0]
    rounds = line.split(':')[1]
    rounds.each_line do |round|
        for i in 2 do
            if round.split(':')[i].include? "green"
                green = round.split(/ /)
                puts green
            end
        end
    end
end