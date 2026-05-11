{
    'name': 'Sélecteur de Prix — Lignes de Devis',
    'version': '19.0.1.0.0',
    'author': 'Prelium',
    'category': 'Sales/Sales',
    'summary': 'Choisir le type de prix sur chaque ligne de devis',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_price_selector_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
