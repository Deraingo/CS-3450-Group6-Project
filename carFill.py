from datetime import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'verdeCars.settings')
django.setup()

def main():
    from verdeCarsPages.models import Car
    # Define a list of cars
    cars = [
        {'make': 'Toyota', 
        'model': 'Camry', 
        'year': '2008', 
        'cost': 50.0, 
        'stranded': False,
        'imageURL': '/media/camry.jpg'},

        {'make': 'Honda', 
        'model': 'Civic', 
        'year': '2009', 
        'cost': 50.0,
        'stranded': False,
        'imageURL': '/media/HondaCivic.jpg'},
        
        {'make': 'Toyota',
        'model': 'Carolla',
        'year': '2009',
        'cost': 50.0,
        'stranded': False,
        'imageURL': '/media/carolla.jpg'},

        {'make': 'Toyota',
        'model': 'Supra',
        'year': '2009',
        'cost': 50.0,
        'stranded': False,
        'imageURL': '/media/supra.jpg'}, 

        {'make': 'Honda',
        'model': 'Civic',
        'year': '2022',
        'cost': 75.0,
        'stranded': False,
        'imageURL': '/media/civic2022.jpg'},

        {'make': 'Nissan',
        'model': 'Skyline',
        'year': '2012',
        'cost': 75.0,
        'stranded': False,
        'imageURL': '/media/skyline.jpg'},  

        {'make': 'Fordd',
        'model': 'Mustang',
        'year': '2022',
        'cost': 75.0,
        'stranded': False,
        'imageURL': '/media/mustang.jpg'},
        
        {'make': 'Audi',
        'model': 'RS5',
        'year': '2022',
        'cost': 75.0,
        'stranded': False,
        'imageURL': '/media/AudiRs5.jpg'},
        
        {'make': 'Lamborghini',
        'model': 'Huracan',
        'year': '2021',
        'cost': 100.0,
        'stranded': False,
        'imageURL': '/media/lambo.jpg'},
        
        {'make': 'Mercedes',
        'model': 'GTR AMG',
        'year': '2019',
        'cost': 100.0,
        'stranded': False,
        'imageURL': '/media/mercedesAmgGtr.jpg'},
        
        {'make': 'Porsche',
        'model': 'Taycan',
        'year': '2022',
        'cost': 110.0,
        'stranded': False,
        'imageURL': '/media/porscheTaycan.jpg'},
        
        {'make': 'Ferarri',
        'model': '296 GTS',
        'year': '2022',
        'cost': 150.0,
        'stranded': False,
        'imageURL': '/media/ferarri.jpg'}
    ]

    # Create Car instances for each car in the list
    for car_data in cars:
        car = Car.objects.create(**car_data)
        car.save()

if __name__ == "__main__":
    main()
