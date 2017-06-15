
class BinarySearch(list):
    """This class inherits from
    the constructor (_init_) which
     initialize an instance variable, length,

    that returns the number of elements in the array
          
    """
    def __init__(self, a, b):
       #constructor method
        # initialize the parent class
        #constructor for the binary seach class
        super(BinarySearch, self).__init__()
        
        # populate the class based on the length and step argument
        for data in range(1, a+1):
            self.append(data * b)

        # define a length of the attributes inthe array
        self.length = len(self)

    def search(self, val):
        """create a method to conduct a binary to find the value
        and return a dictionary with key(count) and value(index)
        where count is the number of time the function iterations and index 
        is the postion of value
        
        """
        # initialize the first and last indices
        first = 0
        last = len(self) - 1
        value_index = 0
        found = False

        # initialize counter to start from the first element
        counter = 0

        # check if val is the first or last element
        if val == self[first]:
            value_index = first
            found = True
        elif val == self[last]:
            value_index = last
            found = True

        # check whether val is in the list
        if val not in self:
            found = True
            value_index = -1

        #while loop to implement binary search algorithm 
        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == val:
                found = True
                value_index = mid
            else:
                # update counter aftereach iteration
                counter += 1  
                if val < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

return {'count': counter, 'index': value_index}
