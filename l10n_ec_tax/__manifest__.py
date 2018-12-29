# -*- coding: utf-8 -*-
# © <2016> <Cristian Salamea>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Ecuador - Taxes',
    'version': '11.0.0.1',
    'category': 'Accounting',
    'author': 'Cristian Salamea',
    'website': 'http://www.ayni.com.ec',
    'license': 'AGPL-3',
    'depends': [
        'l10n_ec_chart',
    ],
    'data': [
        'data/account.tax.group.csv',
        'data/account.tax.csv',
        'data/account.fiscal.position.csv',
        'security/ir.model.access.csv',
        'view/account_tax_report.xml',
        'view/account_report.xml',
        'view/views.xml',
    ]
}
