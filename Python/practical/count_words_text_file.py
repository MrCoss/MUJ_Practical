# Write a Python program to count the occurrences of each word in a given text file.

# Function to count word occurrences in a file
def count_word_occurrences(filename):
    word_count = {}  # Dictionary to store word counts

    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()  # Convert to lowercase and split into words
            for word in words:
                word = word.strip(".,!?()[]{}\"'")  # Remove punctuation
                word_count[word] = word_count.get(word, 0) + 1  # Update count

    return word_count

# Example usage
filename = "C:\\New folder Aamir\\MCA\\Manipal\\Assignments\\Coding_practice\\Python\\practical\\sample.txt" # Name of the text file
word_counts = count_word_occurrences(filename)

# Display word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
