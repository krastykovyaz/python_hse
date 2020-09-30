# рабочие клеят первую стену обоями М минут, каждую следующую клеят на 5 минут дольше, чем предыдущую. За сколько часов рабочие обклеят  n стен. Час считается с первой минуты.
walls =int(input())
total_minute = int(input())
for wall in range(walls):
    total_minute += 5
print(int(total_minute / 60))

