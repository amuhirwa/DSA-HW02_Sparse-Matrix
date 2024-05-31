# Sparse Matrix Operations

This Python script provides functionality for performing operations on sparse matrices, including addition, subtraction, and multiplication. Sparse matrices are matrices with a large number of zero elements, and this script is designed to efficiently handle such matrices.

## Features

- Addition of sparse matrices
- Subtraction of sparse matrices
- Multiplication of sparse matrices
- Parsing input files to create sparse matrices
- Writing results to output files

## Usage

1. **Input Files**: Prepare input files containing sparse matrices in the following format:
   - Each line represents a non-zero element of the matrix in the format `(row, column, value)`.
   - The first 2 lines should specify the dimensions of the matrix in the format `rows=x` and `cols=y`.

2. **Run the Script**: Execute the script `sparse_matrix_operations.py`.
   - You will be prompted to enter the path of the first input file containing the first sparse matrix.
   - After processing the first file, you'll be prompted to enter the path of the second input file if you want to perform an operation with two matrices. If the same file path is entered, the script will perform the operation on the first matrix with itself.
   - You'll then be asked to specify the path for the output file where the result will be written.
   - Finally, you'll be prompted to choose the operation:
     - Enter `1` for addition
     - Enter `2` for subtraction
     - Enter `3` for multiplication

3. **Output File**: The result of the chosen operation will be written to the specified output file.
   - The output file will contain the dimensions of the resulting matrix and its non-zero elements in the format specified for input files.

## Dependencies

This script requires Python 3.x to run.

## Notes

- Ensure that the input files are correctly formatted with the dimensions specified at the beginning and each subsequent line representing a non-zero element in the matrix.
- Invalid input files may lead to errors being raised.
