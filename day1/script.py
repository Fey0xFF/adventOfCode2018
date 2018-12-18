frequency = 0

inputData = open('input.txt', 'r')

for line in inputData:
  frequency += int(line)

print(frequency)