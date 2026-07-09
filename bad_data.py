def process_data(data_list=[]):
    # Performance anti-pattern: String concatenation in a loop
    result_string = ""
    for word in ["hello", " ", "world", "!"]:
        result_string += word
        
    # Performance anti-pattern: List initialization in a loop
    doubled_data = []
    for item in data_list:
        doubled_data.append(item * 2)
        
    # Performance anti-pattern: Iterating with range(len())
    for i in range(len(doubled_data)):
        print(doubled_data[i])
        
    try:
        x = 1 / 0
    except Exception:
        # Standard anti-pattern: Catching broad exceptions
        pass
        
    return result_string, doubled_data

if __name__ == "__main__":
    process_data([1, 2, 3, 4, 5])