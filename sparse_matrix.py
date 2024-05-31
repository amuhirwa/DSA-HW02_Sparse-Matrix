import time

start_time = time.time()

class UtilFunctions:
    @staticmethod
    def ltrim(s):
        """Remove leading spaces and tabs from the string."""
        i = 0
        while s[i] == ' ' or s[i] == '\t':
            i += 1
        return s[i:]
    
    @staticmethod
    def rtrim(s):
        """Remove trailing spaces, newlines, and tabs from the string."""
        i = 1
        while i <= len(s) and (s[-i] == ' ' or s[-i] == '\n' or s[-i] == '\t'):
            i += 1
        return s[:(len(s) + 1) - i]

    @staticmethod
    def trim(s):
        """Remove both leading and trailing spaces, newlines, and tabs from the string."""
        return UtilFunctions.rtrim(UtilFunctions.ltrim(s))

    @staticmethod
    def custom_append(lst, item):
        """Append an item to the list."""
        lst += [item]
        return lst

    @staticmethod
    def str_to_int(s):
        """Convert a string to an integer. Returns False if the string is not a valid integer or exceeds 1023."""
        output = 0
        for i in s:
            if i == ' ':
                return False
            if i == '-':
                continue
            if ord(i) < ord('0') or ord(i) > ord('9') + 1:
                return False
            output = (output * 10) + (ord(i) - ord('0'))
        if s[0] == '-':
            output *= -1
        return output

    @staticmethod
    def merge(array, left, mid, right):
        subArrayOne = mid - left + 1
        subArrayTwo = right - mid

        # Create temp arrays
        leftArray = [0] * subArrayOne
        rightArray = [0] * subArrayTwo

        # Copy data to temp arrays leftArray[] and rightArray[]
        for i in range(subArrayOne):
            leftArray[i] = array[left + i]
        for j in range(subArrayTwo):
            rightArray[j] = array[mid + 1 + j]

        indexOfSubArrayOne = 0  # Initial index of first sub-array
        indexOfSubArrayTwo = 0  # Initial index of second sub-array
        indexOfMergedArray = left  # Initial index of merged array

        # Merge the temp arrays back into array[left..right]
        while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
            if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
            else:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

        # Copy the remaining elements of left[], if any
        while indexOfSubArrayOne < subArrayOne:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
            indexOfMergedArray += 1

        # Copy the remaining elements of right[], if any
        while indexOfSubArrayTwo < subArrayTwo:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

    @staticmethod
    def mergeSort(array, begin, end):
        if begin >= end:
            return

        mid = begin + (end - begin) // 2
        UtilFunctions.mergeSort(array, begin, mid)
        UtilFunctions.mergeSort(array, mid + 1, end)
        UtilFunctions.merge(array, begin, mid, end)


class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

    def insert(self, r, c, val):
        if r >= self.rows or c >= self.cols:
            raise ValueError("Invalid matrix position")
        if val != 0:
            UtilFunctions.custom_append(self.data, [r, c, val])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        UtilFunctions.mergeSort(self.data, 0, len(self.data) - 1)
        UtilFunctions.mergeSort(other.data, 0, len(other.data) - 1)

        apos = bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
            b_row, b_col, b_val = other.data[bpos]

            if (a_row < b_row) or (a_row == b_row and a_col < b_col):
                UtilFunctions.custom_append(result.data, [a_row, a_col, a_val])
                apos += 1
            elif (b_row < a_row) or (b_row == a_row and b_col < a_col):
                UtilFunctions.custom_append(result.data, [b_row, b_col, b_val])
                bpos += 1
            else:
                if a_val + b_val != 0:
                    UtilFunctions.custom_append(result.data, [a_row, a_col, a_val + b_val])
                apos += 1
                bpos += 1

        while apos < len(self.data):
            UtilFunctions.custom_append(result.data, self.data[apos])
            apos += 1

        while bpos < len(other.data):
            UtilFunctions.custom_append(result.data, other.data[bpos])
            bpos += 1

        return result
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        UtilFunctions.mergeSort(self.data, 0, len(self.data) - 1)
        UtilFunctions.mergeSort(other.data, 0, len(other.data) - 1)

        apos = bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
            b_row, b_col, b_val = other.data[bpos]

            if (a_row < b_row) or (a_row == b_row and a_col < b_col):
                UtilFunctions.custom_append(result.data, [a_row, a_col, a_val])
                apos += 1
            elif (b_row < a_row) or (b_row == a_row and b_col < a_col):
                UtilFunctions.custom_append(result.data, [b_row, b_col, -b_val])
                bpos += 1
            else:
                if a_val - b_val != 0:
                    UtilFunctions.custom_append(result.data, [a_row, a_col, a_val - b_val])
                apos += 1
                bpos += 1

        while apos < len(self.data):
            UtilFunctions.custom_append(result.data, self.data[apos])
            apos += 1

        while bpos < len(other.data):
            UtilFunctions.custom_append(result.data, [other.data[bpos][0], other.data[bpos][1], -other.data[bpos][2]])
            bpos += 1

        return result

    def transpose(self):
        result = SparseMatrix(self.cols, self.rows)
        for r, c, val in self.data:
            result.insert(c, r, val)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix dimensions for multiplication")

        result = SparseMatrix(self.rows, other.cols)
        other_t = other.transpose()

        non_zero = {}
        for r, c, val in self.data:
            for r_t, c_t, val_t in other.data:
                if c == r_t:
                    if (r, c_t) not in non_zero:
                        non_zero[(r, c_t)] = 0
                    non_zero[(r, c_t)] += val * val_t
        for (r, c), val in non_zero.items():
            if val != 0:
                result.insert(r, c, val)


        return result

    def print_matrix(self):
        print(f"Dimension: {self.rows} x {self.cols}")
        print("Sparse Matrix: Row Column Value")
        for r, c, val in sorted(self.data):
            print(r, c, val)



def get_parts(string):
    output = []
    if string[0] == '(':
        part = ''
        for s in string[1:-1]:
            if s != ' ' and s != ',' and s != ')':
                part += s
            elif s == ',' or s == ')':
                UtilFunctions.custom_append(output, part)
                part = ''
    return output

def custom_split(string, split_char):
    output = []
    part = ''
    for s in string:
        if s != split_char:
            part += s
        else:
            UtilFunctions.custom_append(output, part)
            part = ''
    UtilFunctions.custom_append(output, part)
    return output

dimensions = {} # Change to other data type

def process_input(input_path):
    with open(input_path, 'r') as f:
        x = 0
        split_line = custom_split(f.readline(), '=')
        dimensions[split_line[0]] = split_line[-1]
        split_line = custom_split(f.readline(), '=')
        dimensions[split_line[0]] = split_line[-1]
        rows = UtilFunctions.str_to_int(dimensions['rows'].strip())
        cols = UtilFunctions.str_to_int(dimensions['cols'].strip())
        matrix = SparseMatrix(rows, cols)
        for line in f:
            try:
                row_num, col_num, value = [UtilFunctions.str_to_int(i.strip()) for i in get_parts(line)]
                matrix.insert(row_num, col_num, value)
            except Exception as e:
                x += 1
                continue
        return matrix
    
def output_results(output_path, results):
    with open(output_path, 'w') as f:
        for i in results:
            f.write(str(i))

if __name__ == "__main__":
    input_file = input("Enter the path of the first matrix file: ")
    print('-'*20, "Processing file", '-'*20)
    matrix1 = process_input(input_file)
    print('-'*20, "Completed", '-'*20)
    second_file = input("Enter the path of the second matrix file: ")
    print('-'*20, "Processing file", '-'*20)
    matrix2 = process_input(second_file)
    print('-'*20, "Completed", '-'*20)
    output_file = input("Enter the path for the output file: ")

    # if input_file == second_file:
    #     matrix1 = matrix2 = process_input(input_file)
    # else:
        
        
    print(time.time() - start_time)
    
    # change to custom sort
    print("Which operation would you like to do:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    choice = input("Enter your choice: ")


    if choice == '1':
        result = matrix1.add(matrix2)
        print(time.time()-start_time)
        output_results(output_file, result.data)
    elif choice == '2':
        result = matrix1.subtract(matrix2)
    elif choice == '3':
        result = matrix1.multiply(matrix2)

# a = SparseMatrix(4, 4)
# b = SparseMatrix(4, 4)

# a.insert(0, 3, 12)
# a.insert(0, 1, 10)
# a.insert(3, 0, 15)
# a.insert(3, 1, 12)
# a.insert(2, 2, 5)
# b.insert(0, 2, 8)
# b.insert(2, 2, 9)
# b.insert(3, 0, 20)
# b.insert(1, 3, 23)
# b.insert(3, 1, 25)

# matrix3 = a.multiply(b)
# matrix3.print_matrix()

# matrix1 = process_input('sample_input_for_students/easy_sample_02_1.txt')
# matrix2 = process_input('sample_input_for_students/easy_sample_02_1.txt')
# matrix2 = process_input('sample_input_for_students/easy_sample_01_2.txt')
