# Write a function that given a positive integer n, returns the length of the longest binary gap of n. Sould return 0 if N doesn't have a binary gap. 
# Write a function:
# def solution(n)
#    pass
def solution(n):

    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Split the binary representation by '1's to find gaps of '0's
    gaps = binary_representation.split('1')
    
    # The last gap is not considered if it ends with '0', so we ignore it
    if binary_representation[-1] == '0':
        gaps.pop()
    
    # Find the length of the longest gap
    longest_gap = max(len(gap) for gap in gaps)
    
    return longest_gap

