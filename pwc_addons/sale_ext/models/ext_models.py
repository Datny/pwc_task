import logging

from odoo import models, fields, api


class SaleOlder(models.Model):
    _inherit = ["sale.order.line"]
    conv_factor = fields.Integer(default=1)
    customer_quantity = fields.Integer()
