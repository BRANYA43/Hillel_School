from flask import Flask, render_template

from utils.support_funcs import load_file, get_average
from utils.unit_converter import UnitConverter


app = Flask(__name__)


@app.route('/')
def get_home():
    students = load_file('hw.csv')
    return render_template('index.html', students=students)


@app.route('/avr_data')
def get_avr_data():
    students = load_file('hw.csv')
    unit_convertor = UnitConverter()
    avr_height_in = get_average(students, 'height')
    avr_weight_po = get_average(students, 'weight')

    avr_height_cm = unit_convertor.convert('in', 'cm', avr_height_in)
    avr_weight_kg = unit_convertor.convert('po', 'kg', avr_weight_po)

    return render_template('avg_data.html', avg_height=avr_height_cm, avg_weight=avr_weight_kg)


app.run(debug=True)
