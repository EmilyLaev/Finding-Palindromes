import sys

# define a method to open file and handle exceptions
def load(file1):
    try:
        with open(file1) as wordfile:
            #seperate words into list format
            loaded_txt = wordfile.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

# label word list and create empty palidrome list
word_list = load('C:\\Users\\Emily\\Python Stuff\\Dictionarywords.txt')
pali_list = []

#run through each word, if palidrome add to pali_list
for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

#print results
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
