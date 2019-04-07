output = 'Yay!'
antennas = []
for i in range(5):
    antennas.append(int(input()))
area = int(input())

for i in range(5):
    for j in range(i+1,5):
        if max(antennas[i],antennas[j])-min(antennas[i],antennas[j]) > area:
            output = ':('
            break
    else:
        continue
    break

print(output)