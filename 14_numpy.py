import numpy as np

if __name__ == '__main__':
    # 1. Creating NumPy arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(0, 10, 2)  # array([0, 2, 4, 6, 8])

    # 2. Basic operations with arrays
    sum_result = arr1 + arr2
    multiply_result = arr1 * 2

    # 3. Universal functions (ufuncs)
    sqrt_result = np.sqrt(arr1)
    sin_result = np.sin(arr2)

    # 4. Reshaping and slicing arrays
    reshaped_arr = arr1.reshape((1, 5))
    sliced_arr = arr2[1:4]

    # 5. Linear algebra operations
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix_product = np.dot(matrix1, matrix2)

    # 6. Statistical operations
    mean_value = np.mean(arr1)
    max_value = np.max(arr2)

    # 7. Random number generation
    random_array = np.random.rand(3, 3)

    # 8. Broadcasting
    broadcasted_result = arr1 + 10

    # 9. Concatenation and stacking
    concatenated_array = np.concatenate((arr1, arr2))
    stacked_array = np.vstack((arr1, arr2))

    # Displaying results
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("\nSum Result:", sum_result)
    print("Multiply Result:", multiply_result)
    print("\nSquare Root Result:", sqrt_result)
    print("Sine Result:", sin_result)
    print("\nReshaped Array:", reshaped_arr)
    print("Sliced Array:", sliced_arr)
    print("\nMatrix Product:", matrix_product)
    print("\nMean Value:", mean_value)
    print("Max Value:", max_value)
    print("\nRandom Array:", random_array)
    print("\nBroadcasted Result:", broadcasted_result)
    print("\nConcatenated Array:", concatenated_array)
    print("Stacked Array:\n", stacked_array)

