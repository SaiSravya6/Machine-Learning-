# Mode Calculation

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())

modes = [key for key, value in freq.items() if value == max_freq]

if len(modes) == 1:
    print("Mode =", modes[0])
else:
    print("Modes =", modes)

\