days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]

month=['január','február','március','április','május','június','július','augusztus','szeptember','október','november', 'december']

month_and_days = []

for i in range(12):
    month_and_days.append(month[i])
    month_and_days.append(days_in_month[i])

print(month_and_days)

print(' '.join(str(month_and_days)))

#-------------------------------------------

numbers = [3,2,6,8,1,5]

max=numbers[0]

for i in range(len(numbers)):
    if max<numbers[i]:
        max=numbers[i]

print(max)

min=numbers[0]

hely=0

for i in range(len(numbers)):
    if min>numbers[i]:
        min=numbers[i]
        hely=i
for i in range(len(numbers)):
    if numbers[i] == min:
        print(i)
print(hely)