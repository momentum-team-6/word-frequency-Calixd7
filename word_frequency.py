STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

punct = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open(file)
    words = file.read().lower()
    

    for ele in punct:
           words = words.replace(ele, " ")
        

    wordslist = words.split()
    

    word_count =[]

    for w in wordslist:
        if w not in STOP_WORDS:
            word_count.append(w)

  
    
    word_frequency = {}

    for w in word_count:
        if w in word_frequency:
            word_frequency[w] += 1
        else:
            word_frequency[w] = 1
            

    sorted_txt= sorted(word_frequency, key=word_frequency.get, reverse=True)
    for num in sorted_txt:
        print(num, word_frequency[num], '*' * word_frequency[num])


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
