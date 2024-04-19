def read_arguments_from_file():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 6:
                raise ValueError("Not enough arguments in file, expected at least 6.")
            return {  # Using a dictionary to map inputs to their labels for clarity
                'SELECT_ATTRIBUTE(S)': lines[0].strip(),
                'NUMBER_OF_GROUPING_VARIABLES(n)': lines[1].strip(),
                'GROUPING_ATTRIBUTES(V)': lines[2].strip(),
                'F-VECT([F])': lines[3].strip(),
                'SELECT_CONDITION-VECT([σ])': lines[4].strip(),
                'HAVING_CONDITION(G)': lines[5].strip(),
            }
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_arguments_manually():
    print("Please enter the 6 arguments for the Phi Operator:")
    return {
        'SELECT_ATTRIBUTE(S)': input("Enter SELECT ATTRIBUTE(S) (e.g., cust, 1_sum_quant, 2_sum_quant, 3_sum_quant): "),
        'NUMBER_OF_GROUPING_VARIABLES(n)': input("Enter NUMBER OF GROUPING VARIABLES(n) (e.g., 3): "),
        'GROUPING_ATTRIBUTES(V)': input("Enter GROUPING ATTRIBUTES(V) (e.g., cust): "),
        'F-VECT([F])': input("Enter F-VECT([F]) (e.g., 1_sum_quant, 1_avg_quant, 2_sum_quant, 3_sum_quant, 3_avg_quant): "),
        'SELECT_CONDITION-VECT([σ])': input("Enter SELECT CONDITION-VECT([σ]) (e.g., 1.state='NY', 2.state='NJ', 3.state='CT'): "),
        'HAVING_CONDITION(G)': input("Enter HAVING_CONDITION(G) (e.g., 1_sum_quant > 2 * 2_sum_quant or 1_avg_quant > 3_avg_quant): ")
    }

def get_phi_operator_arguments():
    choice = input("Do you want to enter arguments manually or from a file? (Type 'manual' or 'file'): ").lower()
    if choice == 'file':
        return read_arguments_from_file()
    elif choice == 'manual':
        return get_arguments_manually()
    else:
        print("Invalid choice. Please enter 'manual' or 'file'.")
        return get_phi_operator_arguments()  # Recursion to handle invalid input

if __name__ == "__main__":
    phi_arguments = get_phi_operator_arguments()
    if phi_arguments is not None:
        print("Phi Operator Arguments:", phi_arguments)
