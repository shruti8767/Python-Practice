#A function to read a file and count the frequency of each word

def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r')as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!?::"\"')
                word_count[word]=word_count.get(word,0)+1

    return word_count

filepath='sample.txt'
word_frequency=count_word_frequency(filepath)
print(word_frequency)