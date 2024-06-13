# -*- coding: utf-8 -*-
{
    'name': "Ave2go",

    'summary': "Módulo realizado por ahigmen0804, SGE 23-24",

    'description': """
        Long description of module's purpose
    """,

    'author': "Adan Higueras Mendoza",
    'website': "https://programadordefp.es/",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '3.0.0',
    'license': "LGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ave2go_views.xml',
        'views/cliente_views.xml',
        'views/reserva_views.xml',
        'views/viaje_views.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
