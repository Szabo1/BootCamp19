def find_max_min(numbers):
    # initialize the variables
    
	max_num = 0
	min_num = numbers[0]

# check for the num in numbers
	for num in numbers:
        # check num is greater than max_num
        # store num in max_num
		if num > max_num:
			max_num = num
        # check if the num is less than max_num 
        # store  the num in min_num   
		elif num < min_num:
			min_num = num
# Check if min_num is eaqual to max_min
# if equal return the length of the number
# return the min_num and the max_num
	if min_num == max_num:
		return [len(numbers)]
	else:
         return [min_num, max_num]
       