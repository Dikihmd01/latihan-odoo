{
    'name': "Real State",
    'version': '1.0',
    'depends': ['base'],
    'author': "Diki Hamdani",
    'category': 'Advertisement',
    'description': """
    This is a module for Real Estate
    """,
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}