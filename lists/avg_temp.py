# calculate average temperature

num_days = int(input("How many no of days:"))

temp = 0

for i in range(1,num_days+1):
    next_day  = int(input("day" +str(i)+ "'s high temp:"))
    temp = temp + next_day

avg = round(temp/num_days,2)
print("Avg =" , str(avg))