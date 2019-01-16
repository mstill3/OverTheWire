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


def shift(input_nums, key_nums):
    print(input_nums)
    print(key_nums)
    nums = []
    for i in range(len(input_nums)):
        nums.append(input_nums[i] - key_nums[i])
    return nums


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
        help="string input")
    ap.add_argument("-k", "--key", required=True,
        help="key to shift by")    

    args = vars(ap.parse_args())
    # display a friendly message to the user
    
    ciphertext = args["input"]
    key = args["key"]

    # to lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # string to char array    
    arr = list(ciphertext)
    karr = list(key)

    # char array to num array
    input_nums = letters_to_nums(arr)
    key_nums = letters_to_nums(karr)

    # shuffled
    nums = shift(input_nums, key_nums)
    #print(nums)

    # num array to char array
    letters = nums_to_letters(nums)
    #print(letters)
    
    # char array to string
    plaintext = "".join(letters)
    print(plaintext)


if __name__=="__main__":
    main()
