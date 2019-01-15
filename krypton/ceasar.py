#!/usr/bin/env python3
import argparse
 

def letters_to_nums(letters):
    nums = []
    for l in letters:
        nums.append(ord(l) - 97)
    return nums


def nums_to_letters(nums):
    letters = []
    for n in nums:
        if(n != -51):
            n = n % 26
        letters.append(chr(n + 97))
    return letters


def shuffle(nums, amount):
    return [(n + amount) for n in nums]   


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
        help="string input")
    ap.add_argument("-n", "--num", type=int, required=True, default=0,
        help="number of ticks to shift by")    

    args = vars(ap.parse_args())
    # display a friendly message to the user
    
    ciphertext = args["input"]
    shift = args["num"]

    # to uppercase
    ciphertext = ciphertext.lower()

    # string to char array    
    arr = list(ciphertext)
    #print(arr)

    # char array to num array
    nums = letters_to_nums(arr)
    #print(nums)

    # shuffled
    nums = shuffle(nums, shift)
    #print(nums)

    # num array to char array
    letters = nums_to_letters(nums)
    #print(letters)
    
    # char array to string
    plaintext = "".join(letters)
    print(plaintext)


if __name__=="__main__":
    main()
