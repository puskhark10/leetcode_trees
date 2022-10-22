#leetcode problem link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
Leetcode problem number: 17
Approach: Backtracking 
"""
from __future__ import annotations

lookup = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

def letter_combinations(digits, n, index, current, combinatns):
    print("lc2")
    if index == n:
        combinatns.append(current)
        return
    
    letters = lookup[digits[index]]
    
    
    for i in range(len(letters)):
        letter_combinations(digits, n, index+1, current+letters[i],combinatns)
    

def letterCombinations(digits: str) -> List[str]:
    print("lc1")
    combinatns = []
    
    if len(digits) == 0:
        return []
    
    letter_combinations(digits, len(digits), 0, "", combinatns)
    
    return combinatns


if __name__ == "__main__":
    print("main")
    digits = input("Enter digits: ")
    all_combinations = letterCombinations(digits)
    print(all_combinations)
    