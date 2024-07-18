# calculate average temperature

num_days = int(input("How many no of days:"))

temp = 0
data = []
for i in range(0,num_days):
    next_day  = int(input("day" +str(i+1)+ "'s high temp:"))
    data.append(next_day)
    temp = temp + next_day


avg = round(temp/num_days,2)
print("Avg =" , str(avg))

above = 0
for i in data:
    if i > avg:
        above +=1
print("Days above average temperature:", above)