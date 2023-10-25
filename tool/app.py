from flask import Flask, render_template, request, jsonify

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    return render_template('database.html')    

@app.route('/generate', methods=['POST'])

def generate_ddl():
    # Get the data from the POST request
    input_ddl = request.form['input_ddl']
    
    
    # Perform some processing on input_ddl to generate the output_ddl
    output_ddl = process_ddl(input_ddl)
    
    # Return the result as JSON
    return jsonify({"output_ddl": output_ddl})

def process_ddl(input_ddl):
    # Your backend processing logic here
    # You can replace this with your actual processing code
    return "Processed DDL: " + input_ddl



@app.route('/getdb', methods=['GET'])
def generate_db():
    db_list = ['db1', 'db2', 'db3']

    # Get the databases
    return jsonify({"db_list": db_list})


@app.route('/gettbl', methods=['GET'])
def generate_tbl():
    # Get the tables  
    db_list = ['db1', 'db2', 'db3']
    # Get the databases
    return jsonify({"db_list": db_list})      



if __name__ == '__main__':
    

    app.run(port=5050,debug=True)
