from multiprocessing.dummy import Pool

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()


def task(word):  # function invoked by each thread
    return word.upper()


thread_pool = Pool(4)

result = thread_pool.map(task, WORDS)
print(f"result: {result}")
