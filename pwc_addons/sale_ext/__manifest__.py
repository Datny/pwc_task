# -*- coding: utf-8 -*-
{
    "name": "sale_ext",
    "summary": """
        Archive for old sales orders""",
    "description": """
        
    """,
    "author": "Robert P",
    "website": "http://localhost",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/templates.xml",
        "views/sale_order_archive_views.xml",
        "views/ext_sale_order_line_views.xml",
        "data/ir_cron.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml"],
}
