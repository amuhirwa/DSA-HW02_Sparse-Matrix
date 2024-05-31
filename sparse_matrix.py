import time
start_time = time.time()

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

    def insert(self, r, c, val):
        if r >= self.rows or c >= self.cols:
            raise ValueError("Invalid matrix position")
        if val != 0:
            self.data.append([r, c, val])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        self.data.sort()
        other.data.sort()

        apos = bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
            b_row, b_col, b_val = other.data[bpos]

            if (a_row < b_row) or (a_row == b_row and a_col < b_col):
                result.data.append([a_row, a_col, a_val])
                apos += 1
            elif (b_row < a_row) or (b_row == a_row and b_col < a_col):
                result.data.append([b_row, b_col, b_val])
                bpos += 1
            else:
                if a_val + b_val != 0:
                    result.data.append([a_row, a_col, a_val + b_val])
                apos += 1
                bpos += 1

        while apos < len(self.data):
            result.data.append(self.data[apos])
            apos += 1

        while bpos < len(other.data):
            result.data.append(other.data[bpos])
            bpos += 1

        return result
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        self.data.sort()
        other.data.sort()

        apos = bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
            b_row, b_col, b_val = other.data[bpos]

            if (a_row < b_row) or (a_row == b_row and a_col < b_col):
                result.data.append([a_row, a_col, a_val])
                apos += 1
            elif (b_row < a_row) or (b_row == a_row and b_col < a_col):
                result.data.append([b_row, b_col, -b_val])
                bpos += 1
            else:
                if a_val - b_val != 0:
                    result.data.append([a_row, a_col, a_val - b_val])
                apos += 1
                bpos += 1

        while apos < len(self.data):
            result.data.append(self.data[apos])
            apos += 1

        while bpos < len(other.data):
            result.data.append([other.data[bpos][0], other.data[bpos][1], -other.data[bpos][2]])
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
                output.append(part)
                part = ''
    return output

def custom_split(string, split_char):
    output = []
    part = ''
    for s in string:
        if s != split_char:
            part += s
        else:
            output.append(part)
            part = ''
    output.append(part)
    return output

dimensions = {} # Change to other data type

def process_input(input_path):
    with open(input_path, 'r') as f:
        x = 0
        split_line = custom_split(f.readline(), '=')
        dimensions[split_line[0]] = split_line[-1]
        split_line = custom_split(f.readline(), '=')
        dimensions[split_line[0]] = split_line[-1]
        rows = int(dimensions['rows'])
        cols = int(dimensions['cols'])
        matrix = SparseMatrix(rows, cols)
        for line in f:
            try:
                row_num, col_num, value = [int(i) for i in get_parts(line)]
                matrix.insert(row_num, col_num, value)
            except Exception as e:
                x += 1
                continue
        return matrix

if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path of the output file: ")
    matrix1 = process_input(input_file)
    matrix2 = process_input(output_file)

    # change to custom sort
    # change to custom int
    # change to custom append

    print("Which operation would you like to do:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    choice = input("Enter your choice: ")

    if choice == '1':
        result = matrix1.add(matrix2)
    elif choice == '2':
        result = matrix1.subtract(matrix2)
    elif choice == '3':
        result = matrix1.multiply(matrix2)


a = SparseMatrix(4, 4)
b = SparseMatrix(4, 4)

a.insert(0, 3, 12)
a.insert(0, 1, 10)
a.insert(3, 0, 15)
a.insert(3, 1, 12)
a.insert(2, 2, 5)
b.insert(0, 2, 8)
b.insert(2, 2, 9)
b.insert(3, 0, 20)
b.insert(1, 3, 23)
b.insert(3, 1, 25)

# matrix1 = process_input('sample_input_for_students/easy_sample_02_1.txt')
# matrix2 = process_input('sample_input_for_students/easy_sample_02_1.txt')
# matrix2 = process_input('sample_input_for_students/easy_sample_01_2.txt')
print((time.time() - start_time) * 1000)

matrix3 = a.subtract(b)
print(matrix3.data[:40])
print((time.time() - start_time) * 1000)