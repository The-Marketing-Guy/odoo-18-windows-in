{
    'name': 'User Sequence',
    'version': '18.0',
    'category': 'Users',
    'summary': 'Assigns a unique sequence number to users for easier identification and search. User sequence, Unique user identifier, User management, Sequence number, User search, User identification, Admin user management, User sequence number, Odoo user search, User sequence assignment, User view, User retrieval, Odoo user management system.',
    'description': '''
        The User Sequence module for Odoo automatically assigns a unique sequence number to each user upon their creation. This sequence number helps administrators easily find and identify users within the system. The sequence is displayed in the user view and can be used in search filters for quick access to specific users. This feature is particularly useful for managing large user bases, making user management more efficient.

        Key Features:
        - Automatically assigns a unique sequence number to each user on creation.
        - Sequence numbers are visible in the user view for easy identification.
        - Enables searching users by their sequence number for quick retrieval.
    ''',
    'author': 'INKERP',
    'website': "http://www.inkerp.com",
    'depends': [],

    'data': [
        'views/res_users_view.xml',
        'data/ir_sequence_data.xml'
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
