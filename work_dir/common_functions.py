import os

history_dir = "assets/"

def write_out_history(numbers, operator, result):

    try:
        with open(os.path.join(history_dir, "history_calc.txt"), "a") as file:
            file.write(f"Operacja: {operator},  z danymi: {numbers}, zakonczona wynikiem: {result}\n")
    except Exception as e:
        print(f"Error in history saving process: {e}")


def read_history():
    try:
        with open(os.path.join(history_dir, "history_calc.txt"), "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Connot access the file")
        return []
    except Exception as e:
        print(f"Error during reading the history: {e}")
        return []

def get_number(command):
    while True:
        try:
            return float(input(command))
        except ValueError:
            print("Error. Data are incorrect")

def read_first_file_portion(file_path, num_bytes=512):
    try:
        with open(file_path, "rb") as file:
            data = file.read(num_bytes)

            print(data)
    except FileNotFoundError:
        print(f"File '{file_path}' doesnt't exist")
    except Exception as e:
        print(f"File readign error: {e}")