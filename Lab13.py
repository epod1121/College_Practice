daily_temp = input("Enter temperatures for each day separated by space: ")
temp_list = []

heat_wave_count = 0
heat_wave = 0
cold_streak_count = 0
cold_streak = 0
avg_temp = 0

for num in daily_temp.split(" "):
    avg_temp += int(num)
    temp_list.append(int(num))

avg_temp = avg_temp / len(temp_list)

for num in temp_list:
    if num > 30:
        heat_wave_count += 1
    else:
        if heat_wave_count >= 3:
            heat_wave += 1
        heat_wave_count = 0
    if num < 15:
        cold_streak_count += 1
        if cold_streak < cold_streak_count:
            cold_streak = cold_streak_count
    else:
        cold_streak_count = 0

if heat_wave_count >= 3:
    heat_wave += 1

print(f"Number of heatwaves: {heat_wave}")
print(f"Longest cold streak: {cold_streak} days")
print(f"Average temperature: {avg_temp: .2f}°C")
