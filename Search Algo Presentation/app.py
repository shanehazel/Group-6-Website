
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

@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    result = None
    steps = None
    infix_expression = None

    if request.method == 'POST':
        infix_expression = request.form['infixExpression']
        result, steps = infix_to_postfix(infix_expression)

    return render_template('infix_postfix.html', result=result, steps=steps, infix_expression = infix_expression)


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



if __name__ == "__main__":
    app.run(debug=True)