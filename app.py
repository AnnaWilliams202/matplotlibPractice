import os
import matplotlib.pyplot as plt

directory = 'files'
filenames = []
numbers = []

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as f:

            number = float(f.read().strip())
            numbers.append(number)
            filenames.append(filename[:-4])

plt.figure(figsize=(10, 6))
plt.plot(filenames, numbers, marker='o',
         linestyle='-', color='blue')
plt.title('Numbers from text files')
plt.xlabel('Filename')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()