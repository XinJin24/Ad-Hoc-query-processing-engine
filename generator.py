import subprocess
def read_arguments_from_file():
    # file_path = input("Enter the file path: ")
    file_path = r"C:\Users\jinxi\Downloads\MF.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        keys = [
            'SELECT ATTRIBUTE(S):',
            'NUMBER OF GROUPING VARIABLES(n):',
            'GROUPING ATTRIBUTES(V):',
            'F-VECT([F]):',
            'SELECT CONDITION-VECT([σ]):',
            'HAVING_CONDITION(G):'
        ]
        parsed_data = {key: [] for key in keys}
        current_key = None

        for line in content:
            line = line.strip()
            if line in keys:
                current_key = line
            elif current_key and line:
                parsed_data[current_key].append(line)

        for key in parsed_data:
            parsed_data[key] = ' '.join(parsed_data[key]).strip()

        if any(len(parsed_data[key]) == 0 for key in keys):
            raise ValueError("Some keys are missing data.")

        return parsed_data

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None
    except ValueError as ve:
        print(ve)
        return None
    except UnicodeDecodeError:
        print("Encoding error: Please check the file encoding. It may not be UTF-8.")
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
        'F-VECT([F])': input(
            "Enter F-VECT([F]) (e.g., 1_sum_quant, 1_avg_quant, 2_sum_quant, 3_sum_quant, 3_avg_quant): "),
        'SELECT_CONDITION-VECT([σ])': input(
            "Enter SELECT CONDITION-VECT([σ]) (e.g., 1.state='NY', 2.state='NJ', 3.state='CT'): "),
        'HAVING_CONDITION(G)': input(
            "Enter HAVING_CONDITION(G) (e.g., 1_sum_quant > 2 * 2_sum_quant or 1_avg_quant > 3_avg_quant): ")
    }


def get_phi_operator_arguments():
    choice = input("Do you want to enter arguments manually or from a file? (Type 'manual' or 'file'): ").lower()
    if choice == 'file':
        return read_arguments_from_file()
    elif choice == 'manual':
        return get_arguments_manually()
    else:
        print("Invalid choice. Please enter 'manual' or 'file'.")
        return get_phi_operator_arguments()


def step1():
    phi_arguments = get_phi_operator_arguments()
    if phi_arguments is not None:
        print("Phi Operator Arguments:", phi_arguments)
        return phi_arguments


def step2(phi_arguments):
    """
    This is the generator code. It should take in the MF structure and generate the code
    needed to run the query. That generated code should be saved to a
    file (e.g. _generated.py) and then run.
    """

    body = """
    for row in cur:
        if row['quant'] > 10:
            _global.append(row)
    """

    # Note: The f allows formatting with variables.
    #       Also, note the indentation is preserved.
    tmp = f"""
import os
import psycopg2
import psycopg2.extras
import tabulate
from dotenv import load_dotenv

# DO NOT EDIT THIS FILE, IT IS GENERATED BY generator.py

def query():
    load_dotenv()

    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    dbname = os.getenv('DBNAME')

    conn = psycopg2.connect("dbname="+dbname+" user="+user+" password="+password,
                            cursor_factory=psycopg2.extras.DictCursor)

    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")

    _global = []
    {body}

    return tabulate.tabulate(_global,
                        headers="keys", tablefmt="psql")

def main():
    print(query())

if "__main__" == __name__:
    main()
    """

    # Write the generated code to a file
    open("_generated.py", "w").write(tmp)
    # Execute the generated code
    subprocess.run(["python", "_generated.py"])


if "__main__" == __name__:
    phi_arguments = step1()
    step2(phi_arguments)