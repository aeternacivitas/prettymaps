from prettymaps import *
from matplotlib import pyplot as plt
palette = ['#433633', '#FF5E5B']
background_c = '#F2F4CB'
dilate = 100
circle = False

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

px = 1/plt.rcParams['figure.dpi']

fig, ax = plt.subplots(figsize = (3840*px, 2160*px), constrained_layout = True)

backup = plot(

    'Paris,France',

    radius = 4000,
    ax = ax,
    postprocessing = postprocessing,
    layers = {
            'perimeter': {},
            'streets': {
                'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
                'width': {
                    'motorway': 5,
                    'trunk': 5,#
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                },
                'circle': False, 'dilate': dilate
            },
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': True, 'circle': False, 'dilate': dilate},
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
                'file_location':'water-polygons-split-4326/water_polygons.shp',
                'buffer':100000,
                'circle':False
            },
            'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': dilate},
            'green': {'tags': {'landuse': ['grass', 'orchard'], 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': dilate},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False}
        },
        drawing_kwargs = {
            #'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'background': {'fc': background_c, 'zorder': -1},
            'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'beach': {'fc': '#FCE19C', 'ec': '#2F3737', 'hatch_c': '#d4d196', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
            'parking': {'fc': background_c, 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
            'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
            'coastline': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch_c': '#85c9e6', 'hatch': 'ooo...', 'lw': 1, 'zorder': 2}
        }
)


plt.savefig('output/paris.png')