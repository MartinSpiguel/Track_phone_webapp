from flask import Blueprint, redirect, render_template, url_for, request, flash
from .locate_phone import get_coordinates, map_coordinates

views = Blueprint('views', __name__)

@views.route('/home/')
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #Do all the proces of getting the phone number and traking it
        try:
            number = request.form.get('number')
            coordinates, loc = get_coordinates(number)
            map_coordinates(coordinates, loc)
            return render_template('location.html')
        except Exception as ex:
            flash('Invalid number, please enter a valid phone number', category='error')
    return render_template('home.html')