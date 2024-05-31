class UtilFunctions:
    @staticmethod
    def ltrim(s):
        """
        Remove leading spaces and tabs from the string.

        Args:
            s (str): The input string.

        Returns:
            str: The trimmed string.
        """
        i = 0
        while s[i] == ' ' or s[i] == '\t':
            i += 1
        return s[i:]
    
    @staticmethod
    def rtrim(s):
        """
        Remove trailing spaces, newlines, and tabs from the string.

        Args:
            s (str): The input string.

        Returns:
            str: The trimmed string.
        """
        i = 1
        while i <= len(s) and (s[-i] == ' ' or s[-i] == '\n' or s[-i] == '\t'):
            i += 1
        return s[:(len(s) + 1) - i]

    @staticmethod
    def trim(s):
        """
        Remove both leading and trailing spaces, newlines, and tabs from the string.

        Args:
            s (str): The input string.

        Returns:
            str: The trimmed string.
        """
        return UtilFunctions.rtrim(UtilFunctions.ltrim(s))

    @staticmethod
    def custom_append(lst, item):
        """
        Append an item to the list.

        Args:
            lst (list): The list to append to.
            item (Any): The item to append.

        Returns:
            list: The list with the appended item.
        """
        lst += [item]
        return lst

    @staticmethod
    def str_to_int(s):
        """
        Convert a string to an integer. Returns False if the string is not a valid integer.

        Args:
            s (str): The string to convert.

        Returns:
            int: The converted integer or False if conversion is not possible.
        """
        output = 0
        for i in s:
            if i == ' ':
                return False
            if i == '-':
                continue
            if i == '.':
                raise(ValueError(f"Input file has wrong format"))
            if ord(i) < ord('0') or ord(i) > ord('9') + 1:
                return False
            output = (output * 10) + (ord(i) - ord('0'))
        if s[0] == '-':
            output *= -1
        return output

    @staticmethod
    def merge(array, left, mid, right):
        """
        Merge two halves of an array for merge sort.

        Args:
            array (list): The array to be merged.
            left (int): The left index.
            mid (int): The middle index.
            right (int): The right index.
        """

        subArrayOne = mid - left + 1
        subArrayTwo = right - mid

        leftArray = [0] * subArrayOne
        rightArray = [0] * subArrayTwo

        for i in range(subArrayOne):
            leftArray[i] = array[left + i]
        for j in range(subArrayTwo):
            rightArray[j] = array[mid + 1 + j]

        indexOfSubArrayOne = 0  
        indexOfSubArrayTwo = 0  
        indexOfMergedArray = left 

        while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
            if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
            else:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

        while indexOfSubArrayOne < subArrayOne:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
            indexOfMergedArray += 1

        while indexOfSubArrayTwo < subArrayTwo:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

    @staticmethod
    def mergeSort(array, begin, end):
        """
        Sort the array using merge sort algorithm.

        Args:
            array (list): The array to be sorted.
            begin (int): The beginning index.
            end (int): The ending index.
        """

        if begin >= end:
            return

        mid = begin + (end - begin) // 2
        UtilFunctions.mergeSort(array, begin, mid)
        UtilFunctions.mergeSort(array, mid + 1, end)
        UtilFunctions.merge(array, begin, mid, end)


class SparseMatrix:
    "Blueprint for sparse matrices."
    def __init__(self, rows, cols):
        """
        Initialize a sparse matrix with given rows and columns.

        Args:
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
        """
        self.rows = rows
        self.cols = cols
        self.data = []

    def insert(self, r, c, val):
        """
        Insert a value into the matrix at specified row and column.

        Args:
            r (int): The row index.
            c (int): The column index.
            val (int): The value to insert.

        Raises:
            ValueError: If the position is invalid.
        """
        if r >= self.rows or c >= self.cols:
            raise ValueError("Invalid matrix position")
        if val != 0:
            UtilFunctions.custom_append(self.data, [r, c, val])

    def add(self, other):
        """
        Add two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to add.

        Returns:
            SparseMatrix: The resulting matrix after addition.

        Raises:
            ValueError: If the dimensions do not match.
        """
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
        """
        Subtract two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to subtract.

        Returns:
            SparseMatrix: The resulting matrix after subtraction.

        Raises:
            ValueError: If the dimensions do not match.
        """
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
        """
        Transposes a matrix meaning it switches it's columns with it's rows.
        Returns:
            SparseMatrix: The resulting matrix after transposing.
        """

        result = SparseMatrix(self.cols, self.rows)
        for r, c, val in self.data:
            result.insert(c, r, val)
        return result

    def multiply(self, other):
        """
        Multiply two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to multiply with.

        Returns:
            SparseMatrix: The resulting matrix after multiplication.

        Raises:
            ValueError: If the dimensions do not allow multiplication.
        """
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
        """
        Print the sparse matrix.

        Prints the dimensions and all non-zero elements in row-column-value format.
        """

        print(f"Dimension: {self.rows} x {self.cols}")
        print("Sparse Matrix: Row Column Value")
        for r, c, val in sorted(self.data):
            print(r, c, val)



def get_parts(string):
    """
    Extract parts of a string within parentheses, separated by commas in the format of (row, column, value).

    Args:
        string (str): The input string.

    Returns:
        list: A list of parts extracted from the string.
    """
    output = []
    if string[0] == '(':
        part = ''
        for s in string[1:]:
            if s != ' ' and s != ',' and s != ')':
                part += s
            elif s == ',' or s == ')':
                UtilFunctions.custom_append(output, part)
                part = ''
    return output

def custom_split(string, split_char):
    """
    Split a string by a specified character.

    Args:
        string (str): The input string.
        split_char (str): The character to split by.

    Returns:
        list: A list of parts after splitting.
    """
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

# Stores dimensions of matrix.
dimensions = {}

def process_input(input_path):
    """
    Process the input file and create a sparse matrix.

    Args:
        input_path (str): The path to the input file.

    Returns:
        SparseMatrix: The created sparse matrix.
    """
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
                line = line.strip()
                if line == '':
                    continue
                row_num, col_num, value = [UtilFunctions.str_to_int(i.strip()) for i in get_parts(line)]
            except:
                print(get_parts(line))
                raise(ValueError(f"Input file has wrong format"))
            try:
                matrix.insert(row_num, col_num, value)
            except Exception as e:
                x += 1
                continue
        return matrix
    
def output_results(output_path, results, r, c):
    """
    Output the results to a file.

    Args:
        output_path (str): The path to the output file.
        results (list): The list of results to write.
        r (int): The number of rows.
        c (int): The number of columns.
    """
    with open(output_path, 'w') as f:
        f.write(f"rows={r}\n")
        f.write(f"cols={c}\n")
        for i in results:
            f.write(f"({i[0]}, {i[1]}, {i[2]})\n")

if __name__ == "__main__":
    input_file = input("Enter the path of the first matrix file: ")
    print('-'*20, "Processing file", '-'*20)
    matrix1 = process_input(input_file)
    print('-'*20, "Completed", '-'*20, '\n')
    second_file = input("Enter the path of the second matrix file: ")
    if input_file == second_file:
        matrix2 = matrix1
    else:
        print('-'*20, "Processing file", '-'*20)
        matrix2 = process_input(second_file)
    print('-'*20, "Completed", '-'*20)
    output_file = input("Enter the path for the output file: ")
    
    print("Which operation would you like to do:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    choice = input("Enter your choice: ")

    print('-'*20, "Performing operation", '-'*20)
    if choice == '1':
        result = matrix1.add(matrix2)
        output_results(output_file, result.data, result.rows, result.cols)
    elif choice == '2':
        result = matrix1.subtract(matrix2)
        output_results(output_file, result.data, result.rows, result.cols)
    elif choice == '3':
        result = matrix1.multiply(matrix2)
        output_results(output_file, result.data, result.rows, result.cols)
    else:
        print("Not a valid operation.")
        
