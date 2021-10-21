import vsketch
palette = ['#2E292E', '#F37422', '#F9A41B', '#79A9AB']
background_c = '#A8AE95'
dilate = 500

from prettymaps import *
import matplotlib.font_manager as fmare
from matplotlib import pyplot as plt

#city_dict = {"Kabul":"Afghanistan","Tirana":"Albania","Alger":"Algeria","Fagatogo":"American Samoa","Andorra la Vella":"Andorra","Luanda":"Angola","The Valley":"Anguilla","Saint John's":"Antigua and Barbuda","Buenos Aires":"Argentina","Yerevan":"Armenia","Oranjestad":"Aruba","Canberra":"Australia","Wien":"Austria","Baku":"Azerbaijan","Nassau":"Bahamas","al-Manama":"Bahrain","Dhaka":"Bangladesh","Bridgetown":"Barbados","Minsk":"Belarus","Brussels":"Belgium","Belmopan":"Belize","Porto-Novo":"Benin","Hamilton":"Bermuda","Thimphu":"Bhutan","La Paz":"Bolivia","Sarajevo":"Bosnia and Herzegovina","Gaborone":"Botswana","Brasília":"Brazil","Bandar Seri Begawan":"Brunei","Sofia":"Bulgaria","Ouagadougou":"Burkina Faso","Bujumbura":"Burundi","Phnom Penh":"Cambodia","Yaound":"Cameroon","Ottawa":"Canada","Praia":"Cape Verde","George Town":"Cayman Islands","Bangui":"Central African Republic","N'Djam":"Chad","Santiago de Chile":"Chile","Peking":"China","Flying Fish Cove":"Christmas Island","West Island":"Cocos (Keeling) Islands","Santaf":"Colombia","Moroni":"Comoros","Brazzaville":"Congo","Avarua":"Cook Islands","San Jos":"Costa Rica","Zagreb":"Croatia","La Habana":"Cuba","Nicosia":"Cyprus","Praha":"Czech Republic","Copenhagen":"Denmark","Djibouti":"Djibouti","Roseau":"Dominica","Santo Domingo de Guzm":"Dominican Republic","Dili":"East Timor","Quito":"Ecuador","Cairo":"Egypt","San Salvador":"El Salvador","London":"England"}
#city_dict = {"Talinn": "Estonia"}
#city_dict = {"Suva":"Fiji", "Santo Domingo":"Dominican Republic", "Djibouti":"Djibouti","Bogota":"Colombia",}
#reverse_city = {'Bairiki':'Kiribati', 'Banjul':'Gambia', 'Basse-Terre':'Guadeloupe','Beirut':'Lebanon', 'Bissau':'Guinea-Bissau','Cayenne':'French Guiana','ciudad de guatemala':'guatemala','Conakry':'Guinea','Dili':'East Timor','Georgetown':'Guyana','Gibraltar':'Gibraltar','Kingston':'Jamaica','Kuwait City':'Kuwait','Libreville':'Gabon','Luxembourg City':'Luxembourg','New Delhi':'India'}
#reverse_city = {'Victoria':'Hong Kong'}
city_dict = {"39.9555":"116.2917"}
circle = False
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

for key in city_dict:
    city, country = key, city_dict[key]
    print(f'Working on {city} on country {country}')
    try:
        layers = plot(
            city+', '+country,
            radius = 3500,
            ax = ax,
            layers = {
                    'perimeter': {},
                    'streets': {
                        'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
                        'width': {
                            'motorway': 5,
                            'trunk': 5,
                            'primary': 4.5,
                            'secondary': 4,
                            'tertiary': 3.5,
                            'residential': 3,
                            'service': 2,
                            'unclassified': 2,
                            'pedestrian': 2,
                            'footway': 1,
                        },
                        'circle': False, 'dilate': dilate,
                        'retain_all': True
                    },
                    'railway':{
                        'custom_filter': '["railway"~"rail|light_rail|subway|tram|disused|construction|abandoned|monorail|narrow_gauge"]',
                        'width':1,
                        'circle':circle,
                        'buffer':3000,
                        'retain_all':True,
                        'dilate':dilate
                    },
                    'building': {'tags': {'building': True, 'railway':'platform', 'landuse': 'construction'}, 'union': True, 'circle': False, 'dilate': dilate},
                    'water': {
                        'tags':{
                            'waterway': True,
                            'water': True,
                            'harbour': True,
                            'marina': True,
                            'bay': True,
                            'river': True
                        },
                        'dilate':dilate,
                        'circle': False,
                    },
                    'coastline':{
                        'file_location':'water-polygons-split-4326/water_polygons.shp', # if on windows make sure to change the path ( add ./ at the beginning)
                        'buffer':100000,
                        'circle':False,
                        'dilate':dilate,
                    },
                    'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': dilate},
                    'green': {'tags': {'landuse': ['grass', 'orchard', 'village_green'], 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': dilate},
                    'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False},
                },
                drawing_kwargs = {
                    'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
                    'background': {'fc': background_c, 'zorder': -1},
                    'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
                    'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
                    'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
                    'beach': {'fc': '#FCE19C', 'ec': '#2F3737', 'hatch_c': '#d4d196', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
                    'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
                    'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
                    'railway': {'fc': '#343a40', 'ec': '#343a40', 'alpha': 1, 'lw': 0, 'zorder': 2},
                    'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
                    'coastline': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch_c': '#85c9e6', 'hatch': 'ooo...', 'lw': 1, 'zorder': 2}
                },
        )
    except Exception:
        print('Something wrong, pass')
        pass
    city = city.replace(" ","_")
    country = country.replace(" ","_")

    #Set bounds
    xmin, ymin, xmax, ymax = layers['perimeter'].bounds
    dx, dy = xmax-xmin, ymax-ymin
    ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
    ax.set_ylim(ymin-.06*dy, ymax+.02*dy)

    plt.savefig('custom/{}_{}rail3.png'.format(city, country))   # if on windows make sure to change the path ( add ./ at the beginning)