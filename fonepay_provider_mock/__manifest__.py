# -*- coding: utf-8 -*-
{
    'name': "Fonepay Payment Provider",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose
    """,
    'author': "Aman Manandhar",
    'category': 'payment',
    'version': '18.0.1.0.0',
    'depends': ['payment'],
    'assets':{
        'web.assets_backend': [
            'fonepay_provider_mock/static/src/js/notification.js',
            'fonepay_provider_mock/static/src/xml/notification.xml',
        ],
    },
    'data': [
        'data/payment_provider_data.xml',
        'views/payment_provider_views.xml',
    ],
    'installable': True,
}

