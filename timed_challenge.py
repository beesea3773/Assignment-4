# Pick one question from timed_challenge.txt
# Paste the question as a comment below
#3. Remove Duplicates (Keep Order)
#Return the values in the order they first appeared, without duplicates.
#Input: ["apple", "banana", "apple", "kiwi", "banana"]
#Output: ["apple", "banana", "kiwi"]

def remove_duplicates(values):
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


items = ["apple", "banana", "apple", "kiwi", "banana"]
print(remove_duplicates(items))

print(remove_duplicates([]))
print(remove_duplicates(["apple"]))
print(remove_duplicates(["apple", "apple", "apple"]))
print(remove_duplicates(["apple", "banana", "apple", "kiwi", "banana"]))

# Set a timer for 30 minutes and complete the question!


"""
For this timed challenge, I chose the Remove Duplicates problem. 
I decided to use a set along with a list to solve the problem. The set was useful because it allowed me 
to quickly check if I had already seen a value before. The list was needed because I still had to keep the 
values in the same order that they originally appeared. As I went through each value, I checked the set first.
 If the value was not already there, I added it to the set and then added it to the result list.

The 30-minute time limit made me focus on finding a solution that was simple and easy to understand instead
 of trying to make the code more complicated. I knew that using only a list would work, but checking 
 the entire list every time could become slower with larger amounts of data. Using a set made checking
 for duplicates much faster.

One trade-off with my solution is that I had to use two data structures instead of one,
 which uses some extra memory. However, I think this was a good trade-off because the solution 
 is faster and still keeps the original order of the values. I also tested the solution with an 
 empty list, one value, repeated values, and a normal list to make sure it worked correctly in different situations.
"""