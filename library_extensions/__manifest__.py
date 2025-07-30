{
    'name': "Library Extensions",
    'version': '17.0.1.0.0',
    'author': "Your Name",
    'category': 'Library',
    'summary': "Extends library module with authors and categories",
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_book_category_views.xml',
    ],
    'installable': True,
    'application': False,
}