from multiprocessing import Pool, freeze_support

with open('../DATA/words.txt') as words_in:
    all_words = words_in.read().splitlines()  # create list of 173K words

def task(word):  # function invoked by each thread
    return word.upper()

if __name__ == '__main__':
    freeze_support()

    proc_pool = Pool(16)

    result = proc_pool.map(task, all_words)
    print(f"result: {result[:50]}")
