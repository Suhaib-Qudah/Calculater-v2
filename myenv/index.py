from flask import Flask, render_template, url_for, request, redirect
import math

# Create an instance of the Flask application
app = Flask(__name__)
#Create a secret key 
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

            
operations  = [
         {'value':'add','title':'Add +'},
        {'value':'subtract', 'title':'Subtract -'},
        {'value':"multiply", 'title':'Multiply *'},
        {'value':"divide", 'title':'Divide /'},
        {'value':"absolute", 'title':'Absolute |X|'},
        {'value':"to_power", 'title':'To Power ^'},
        {'value':"sqrt", 'title':'Square root(√)'},
        {'value':"sin", 'title':'Sin (θ)'},
        {'value':"cos", 'title':'Cos (θ)'},
        {'value':"tan", 'title':'Tan (θ)'},
        {'value':"log", 'title':'Log10 (X)'},
        {'value':"ln", 'title':'ln (X)'},
        {'value':"e", 'title':'e^'},
        {'value':"factorial", 'title':'x!'},


]
@app.route('/' , methods= ["POST", "GET"])
@app.route('/home' , methods= ["POST", "GET"])
def home():

    if request.method == 'POST':
        number1 = float(request.form['number1'])   # read the value from the first number input
        number2 = float(request.form['number2'])  # read the value from the second number input
        operation = str(request.form['menu'])

        if(operation == 'add'):
            answer = number1 + number2
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'subtract'):
            answer = number1 - number2
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'multiply'):
            if (number2 == 0 or number1 == 0):
                error ="One of the numbers is zero. The answer is definitely zero."
                return render_template('error.html' , error = error )
            answer = number1 * number2
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'divide'):
            if (number2 == 0):
                error ="Division by zero."
                return render_template('error.html' , error = error )
            answer = number1 / number2
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'to_power'):
            answer = number1**number2
            return render_template('index.html' , answer = answer , operations = operations)
        elif(operation == 'sqrt'):
            if(number1 < 0):
                error ="In Square root you can't use negative numbers. Change your number please..."
                return render_template('error.html' , error = error )
            answer = math.sqrt(number1)
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'sin'):
            answer = round(math.sin(math.radians(number1)),2)
            return render_template('index.html' , answer = answer , operations = operations)
        elif(operation == 'cos'):
            answer = round(math.cos(math.radians(number1)),2)
            return render_template('index.html' , answer = answer , operations = operations)
        elif(operation == 'tan'):
            answer = round(math.tan(math.radians(number1)),2)
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'absolute'):
            answer = abs(number1)
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'log'):
            answer = math.log10(number1)
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'ln'):
            e = 2.718281828
            answer =  float(math.log( 10 , e ) )
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'e'):
            e = 2.718281828
            answer =  pow(e , number1)
            return render_template('index.html' , answer = answer, operations = operations )
        elif(operation == 'factorial'):
            answer =  math.factorial(number1)
            return render_template('index.html' , answer = answer, operations = operations )        
        

    else:

        return render_template('index.html')
pass
