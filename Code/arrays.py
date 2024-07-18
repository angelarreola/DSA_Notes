new_list = [1,2,3]

first_value = new_list[0]

if 1 in new_list: # Linear Search, it used the contains method.
    print(True);

for n in new_list: # Also Linear search
    if n == 1:
        print(True)
        break

# Insert values
numbers = [1,2,3]

# True Insert
# [5,1,3,2,6]
# We insert 4 in the [0] position
# [4,5,1,3,2,6] // Linear Runtime
numbers.insert(0, 4)

# Appending
# [5,1,3,2,6]
# We append 7 on the end of the list.
# [5,1,3,2,6,7] // Generally Constant Time, depends on the lenguage implementation.
numbers.append(5)
numbers.append(200) # List Resize following the growth pattern : 0,4,8,16,25,35

numbers.extend([4,5,6]) # Run-time of O(k) where k is the number of elements in the list that we're adding.

# Delete - Linear Runtime O(n)
# When we delete an element, the other elements will need to be shifted either to the right or to the left.




print(numbers)