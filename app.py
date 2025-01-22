#Install neccessary libraries
from flask import Flask, render_template, request


app = Flask(__name__)

#Route for the index page.
@app.route('/')
def index():
    return render_template('index.html')

#Route for the calculation page.
@app.route('/calculate', methods=['POST'])
def calculate():
    #Get first car details
    first_car_year = int(request.form['first_car_year'])
    first_car_make = request.form['first_car_make']
    first_car_model = request.form['first_car_model']
    first_car_curb_weight = float(request.form['first_car_curb_weight'])
    first_car_horsepower = float(request.form['first_car_horsepower'])
    first_power_weight_ratio = first_car_curb_weight / first_car_horsepower
    
    #Get second car details.
    second_car_year = int(request.form['second_car_year'])
    second_car_make = request.form['second_car_make']
    second_car_model = request.form['second_car_model']
    second_car_curb_weight = float(request.form['second_car_curb_weight'])
    second_car_horsepower = float(request.form['second_car_horsepower'])
    second_power_weight_ratio = second_car_curb_weight / second_car_horsepower
    
    #Calculate percentage difference.
    percentage_difference = -1 * (second_power_weight_ratio - first_power_weight_ratio) / first_power_weight_ratio * 100
    performance_comparison_term = "better" if percentage_difference >= 0 else "worse"
    
    return render_template('result.html', 
                           first_car_year=first_car_year, first_car_make=first_car_make, first_car_model=first_car_model, 
                           first_power_weight_ratio=first_power_weight_ratio,
                           second_car_year=second_car_year, second_car_make=second_car_make, second_car_model=second_car_model, 
                           second_power_weight_ratio=second_power_weight_ratio,
                           percentage_difference=abs(percentage_difference), performance_comparison_term=performance_comparison_term)

if __name__ == '__main__':
    app.run(debug=True)
