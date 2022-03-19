#from Locate_phone.locate_phone import get_coordinates, map_coordinates, open_map_file
#from Locate_phone.number import number
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)