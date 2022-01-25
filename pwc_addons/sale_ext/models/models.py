# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOlderArchive(models.Model):
    _name = "sale.order.archive"

    name = fields.Char()
    customer = fields.Many2one("res.partner")
    sale_person = fields.Many2one("res.users")
    order_currency = fields.Many2one("res.currency")
    order_total_amount = fields.Monetary(currency_field="order_currency")
    count_of_order_lines = fields.Integer()
    create_date = fields.Date(readonly=True, default=fields.Date.context_today)
