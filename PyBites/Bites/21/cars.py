#PyBites
#https://codechalleng.es/bites/21/12869/

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated list of jeep models (original order)"""
    return ', '.join(cars.get('Jeep'))


def get_first_model_each_manufacturer():
    return [models[0] for constructor,models in cars.items()]


def get_all_matching_models(grep='trail'):
    return sorted([model for constructor, models in cars.items() for model in models if grep.lower() in model.lower()])

def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    return {constructor: sorted(models) for constructor, models in cars.items()}
