# fizzbuzz_list = [
#     "FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else
#     "Fizz" if i % 3 == 0 else
#     "Buzz" if i % 5 == 0 else
#     i for i in range(1, 101)]

# print(fizzbuzz_list)
# print("____________________________________")
# fizz2 = [
#     'FizzBuzz' if (n % 15 == 0) else 
#     ('Fizz' if (n % 3 == 0) else
#      'Buzz' if (n % 5  == 0) else
#      n) for n in range(1, 101)]
# print(fizz2)

# def primes_gen():
#     num = 2
#     while True:
#         prime_num = True
#         for i in range(2, num):  
#             if num % i == 0:
#                 prime_num = False
#                 break
#         if prime_num:
#             yield num 
#         num += 1

# gen = primes_gen()
# for num in range(10): print(next(gen),
#      end='  ')

# def unique_letters(string):
#     seen = set()
#     for letter in string:
#         if letter not in seen:
#             seen.add(letter)
#             yield letter

# for letter in unique_letters('hhhello'):
#     print(letter, end=' ')


def outer(msg): lang =
    'Python' def inner():
        print(lang, msg)
    return inner

my_func = outer('is fun!!!')
my_func()	# output: 'Python is fun!!!'
