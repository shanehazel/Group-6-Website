from flask import Flask, render_template, request
import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from flask import Flask, render_template, request
from InfixPostfix import infix_to_postfix  
from graphMRT import Graph
from bubble_sort_algo import bubble_sort
from selection_sort_algo import selection_sort
from insertion_sort_algo import insertion_sort
from merge_sort_algo import merge_sort
from quick_sort_algo import quick_sort
import time
import timeit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/profile')
def profile():  
    return render_template('profile.html')

@app.route('/home')
def contact():
    return render_template('home.html')

@app.route('/searchAlgorithm')
def searchAlgorithm():
    return render_template('searchAlgorithm.html')

@app.route('/hash_algo')
def hash_algo():
    return render_template('hash.html')


@app.route('/one', methods=["GET", "POST"])
def one():
    
    numbers = range(1, 101)
    test_data = ", ".join(map(str, numbers))
    #print(test_data)
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                #arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("one.html", result=result, search_type=search_type, execution_time=execution_time,test_data=test_data)
        except ValueError:
            return render_template("one.html", error="Invalid input. Ensure the array and target are integers.")
    

    return render_template("one.html",test_data=test_data)


@app.route('/two', methods=["GET", "POST"])
def two():
    
    numbers = range(1, 1001)
    test_data = ", ".join(map(str, numbers))
    #print(test_data)
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                #arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("two.html", result=result, search_type=search_type, execution_time=execution_time,test_data=test_data)
        except ValueError:
            return render_template("two.html", error="Invalid input. Ensure the array and target are integers.")
    

    return render_template("two.html",test_data=test_data)

@app.route('/three', methods=["GET", "POST"])
def three():
    
    numbers = range(1, 10001)
    test_data = ", ".join(map(str, numbers))
    #print(test_data)
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                #arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("three.html", result=result, search_type=search_type, execution_time=execution_time,test_data=test_data)
        except ValueError:
            return render_template("three.html", error="Invalid input. Ensure the array and target are integers.")
    

    return render_template("three.html",test_data=test_data)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)
    #result_recursive = exponential_search_recursive(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
       # "recursive_search_result": result_recursive
    })

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/results1')
def results1():
    return render_template('results1.html')


@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    result = None
    steps = None
    infix_expression = None

    if request.method == 'POST':
        infix_expression = request.form['infixExpression']
        result, steps = infix_to_postfix(infix_expression)

    return render_template('infix_postfix.html', result=result, steps=steps, nfixExpression = infix_expression)


@app.route('/queue_dequeue')
def queue_deque():  
    return render_template('q_dq.html')\


queue = []
@app.route('/queue_dequeue', methods=['GET', 'POST'])
def queue_operations():
    Enqueue = None
    Dequeue = None

    if request.method == 'POST':

        if request.form.get('enqueue', ''):
            data = str(request.form.get('inputString', ''))
            queue.append(data)

        elif request.form.get('dequeue', ''):
            if queue:
                Dequeue = queue.pop(0)

    return render_template('q_dq.html', Enqueue=queue, Dequeue=Dequeue)

# Hash table initialization
hash_table = [[] for _ in range(32)]

# Hash functions
def hash_function_1(k, m):
    return k % m

def hash_function_2(k, m):
    return ((1731 * k + 520123) % 524287) % m

# Default hash method of Python
def hash_function_3(s, m):
    return hash(s) % m

# Function to insert a key into the hash table
def insert_key(key, hash_function, m):
    k = sum(ord(char) for char in key)
    index = hash_function(k, m)
    hash_table[index].insert(0, key)

# Function to delete a key from the hash table
def delete_key(key, hash_function, m):
    k = sum(ord(char) for char in key)
    index = hash_function(k, m)
    if key in hash_table[index]:
        hash_table[index].remove(key)

# Function to handle the input commands
def process_commands(commands, hash_function, m):
    for command in commands:
        if command.startswith("del "):
            delete_key(command[4:], hash_function, m)
        else:
            insert_key(command, hash_function, m)


# Function to generate the output format
def generate_output():
    output = []
    for i, slot in enumerate(hash_table):
        output.append(f"{i}: {slot}")
        output.append(f"\n")
    return output


@app.route('/hash_algo', methods=['GET', 'POST'])
def hash_algo_form():
    if request.method == 'POST':
        selected_hash_function = request.form['hash_function']
        num_commands = int(request.form['num_commands'])
        commands = request.form['commands'].split('\n')
        
        if selected_hash_function == 'hash_function_1':
            process_commands(commands, hash_function_1, 32)
        elif selected_hash_function == 'hash_function_2':
            process_commands(commands, hash_function_2, 32)
        elif selected_hash_function == 'hash_function_3':
            process_commands(commands, hash_function_3, 32)

    output = generate_output()
    return render_template('hash.html', output=output)

@app.route('/graph_algo', methods=['GET', 'POST'])
def graph_algo():
    note1 = None
    note2 = None
    note3 = None
    # Creating a graph for MRT Line 3 and LRT Lines 1 and 2
    manila_graph = Graph()

    stations_mrt_line3 = ["North Avenue", "Quezon Avenue", "Kamuning", "Araneta Center-Cubao MRT", "Santolan-Anapolis", "Ortigas", "Shaw Boulevard", "Boni", "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"]
    stations_lrt_line1 = ["Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa", "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "D. Jose", "Carriedo", "Central Terminal", "United Nations", "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"]
    stations_lrt_line2 = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go-Belmonte", "Araneta Center-Cubao LRT2", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

    for station in stations_mrt_line3 + stations_lrt_line1 + stations_lrt_line2:
        manila_graph.add_station(station, set())

    # MRT Line 3 connections
    manila_graph.add_connection("North Avenue", "Quezon Avenue", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Quezon Avenue", "Kamuning", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Kamuning", "Araneta Center-Cubao MRT", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Araneta Center-Cubao MRT", "Santolan-Anapolis", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Santolan-Anapolis", "Ortigas", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Ortigas", "Shaw Boulevard", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Shaw Boulevard", "Boni", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Boni", "Guadalupe", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Guadalupe", "Buendia", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Buendia", "Ayala", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Ayala", "Magallanes", 1, {Graph.MRT_LINE_3})
    manila_graph.add_connection("Magallanes", "Taft Avenue", 1, {Graph.MRT_LINE_3})

    #LRT Line 1 connections
    manila_graph.add_connection("Roosevelt", "Balintawak", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Balintawak", "Monumento", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Monumento", "5th Avenue", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("5th Avenue", "R. Papa", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("R. Papa", "Abad Santos", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Abad Santos", "Blumentritt", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Blumentritt", "Tayuman", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Tayuman", "Bambang", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Bambang", "D. Jose", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("D. Jose", "Carriedo", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Carriedo", "Central Terminal", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Central Terminal", "United Nations", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("United Nations", "Pedro Gil", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Pedro Gil", "Quirino", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Quirino", "Vito Cruz", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Vito Cruz", "Gil Puyat", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Gil Puyat", "Libertad", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Libertad", "EDSA", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("EDSA", "Baclaran", 1, {Graph.LRT_LINE_1})

    # LRT Line 2 connections
    manila_graph.add_connection("Recto", "Legarda", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Legarda", "Pureza", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Pureza", "V. Mapa", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("V. Mapa", "J. Ruiz", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("J. Ruiz", "Gilmore", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Gilmore", "Betty Go-Belmonte", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Betty Go-Belmonte", "Araneta Center-Cubao LRT2", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Araneta Center-Cubao LRT2", "Anonas", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Anonas", "Katipunan", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Katipunan", "Santolan", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Santolan", "Marikina", 1, {Graph.LRT_LINE_2})
    manila_graph.add_connection("Marikina", "Antipolo", 1, {Graph.LRT_LINE_2})

    # Additional connections based on corrections
    manila_graph.add_connection("Recto", "D. Jose", 1, {Graph.LRT_LINE_1, Graph.LRT_LINE_2})
    manila_graph.add_connection("D. Jose", "Carriedo", 1, {Graph.LRT_LINE_1})
    manila_graph.add_connection("Taft Avenue", "EDSA", 1, {Graph.MRT_LINE_3, Graph.LRT_LINE_1})
    manila_graph.add_connection("Araneta Center-Cubao MRT", "Araneta Center-Cubao LRT2", 1, {Graph.MRT_LINE_3, Graph.LRT_LINE_2})
    
    if request.method == 'POST':
        start_station = request.form.get('start_station', '')
        end_station = request.form.get('end_station', '')
        shortest_distance, shortest_path, lines_taken = manila_graph.shortest_path(start_station, end_station)

        if shortest_distance != float('inf'):
            transfer_station = None
            
            # Find the station where the transfer occurs
            for i in range(len(shortest_path) - 1):
                current_station = shortest_path[i]
                next_station = shortest_path[i + 1]
                if manila_graph.station_lines[current_station] != manila_graph.station_lines[next_station]:
                    transfer_station = next_station
                    break

            # Print the result with the transfer station
            if transfer_station:
                note1 = f"Shortest distance from {start_station} to {end_station}: {shortest_distance} stations."
                note2 = f"Shortest path: {shortest_path}"
              
    
                
            else:
                note1 = f"Shortest distance from {start_station} to {end_station}: {shortest_distance} stations."
                note2 = f"Shortest path: {shortest_path}"
                
        else:
            note1 = f"No path found from {start_station} to {end_station}"
            note2 = ""
            
    return render_template('graph_mrt.html', result=note1, result1=note2)


@app.route('/sorting_algo', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        input_array = request.form.get('inputArray')

        
        if input_array is None or input_array.strip() == "":
            return render_template('SortingAlgo.html', error_message="Please enter valid input.")

        input_array = list(map(int, input_array.split(',')))

        selected_algorithm = request.form.get('algorithm')

        total_time = 0
        num_iterations = 10  

        for _ in range(num_iterations):
            start_time = time.time()

            if selected_algorithm == 'bubble':
                sorted_array = bubble_sort(input_array)
            elif selected_algorithm == 'selection':
                sorted_array = selection_sort(input_array)
            elif selected_algorithm == 'insertion':
                sorted_array = insertion_sort(input_array)
            elif selected_algorithm == 'merge':
                sorted_array = merge_sort(input_array)
            elif selected_algorithm == 'quick':
                sorted_array = quick_sort(input_array)
            else:
                sorted_array = input_array 

            end_time = time.time()
            total_time += end_time - start_time

        elapsed_time = total_time / num_iterations  

        return render_template('SortingAlgo.html', result=sorted_array, elapsed_time=elapsed_time)


    return render_template('SortingAlgo.html')


if __name__ == "__main__":
    app.run(debug=True)