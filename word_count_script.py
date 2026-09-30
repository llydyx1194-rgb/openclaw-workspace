import os
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return len(words)

dir_path = 'your_directory_here'
word_counts = {}
for filename in os.listdir(dir_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(dir_path, filename)
        word_count = count_words(file_path)
        word_counts[filename] = word_count

counted_word_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for file_name, count in counted_word_list:
    print(f'{file_name}: {count}')