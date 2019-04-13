# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Checkin',
    'summary': 'Check-in',
    'license': 'AGPL-3',
    'sequence': 1,
    'description': """
        Mobile Check-in
    """,
    'website': 'https://dnpcorp.vn',
    'depends': ['base'],
    'data': [
        'views/checkin_views.xml',
        'views/user_checkin_views.xml',
        'views/menu.xml'
    ],
    'css': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}