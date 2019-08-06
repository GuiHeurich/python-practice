import sys

def read_file(filename):
    f = open(filename)
    return f.read()

def count_words(filename):
    words = {}
    list_of_lines = read_file(filename).split()
    for word in list_of_lines:
        if word in words:
            words[word] += 1
        else:
            words[word.lower()] = 1

    sorted_by_count = []

    for word in sorted(words, key=words.__getitem__, reverse=True):
        sorted_by_count.append('%s %s' % (word, words[word]))

    for i in range(0, 40):
        print sorted_by_count[i]

    print_total(words)

def print_total(words):
    length = len(words)
    print 'Total word count: %s' % (length)

def main():
  filename = sys.argv[1]
  count_words(filename)

if __name__ == '__main__':
  main()
