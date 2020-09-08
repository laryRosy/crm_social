# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Social',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 5,
    'summary': 'Add social networks data to customers profile',
    'description': "",
    'depends': [
        'crm',
    ],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
