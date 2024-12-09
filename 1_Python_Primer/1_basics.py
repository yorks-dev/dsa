obj1 = 10
obj2 = obj1

print(obj2)  # REF DONE

bool_false = bool(0)  # anything other than 0 True
print(bool_false)
# for strings lists Empty - False else True

### SETS ###
# Sets are most useful in looking up if a data is there in a set
# They use hashtables
# ONlY IMMUTABLE objects can be added to sets

## DICT ##
pairs = [("ga", "Irish"), ("de", "German")]
print(dict(pairs))


## Exercise
# 1. Calculate the size of the file manually
# File name - test_file.txt

fp = open("./comfort-dark-0.1.0.vsix", "r")
fp.seek(0, 2)  # 2 stands for os.SEEK_END (end of file)
print(f"Size = {fp.tell() / 1000} KB")
