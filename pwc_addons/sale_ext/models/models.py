# -*- coding: utf-8 -*-
import datetime
import logging
from dateutil.relativedelta import relativedelta

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

    def _cron_archive_and_remove_selected(self):
        """Creates new „sale.order.archive” object for all orders (sale.order) older than 7 days  and delete archived
        „sale.order” object"""
        _logger = logging.getLogger(__name__)
        old_sale_orders = (
            self.env["sale.order"]
            .search([])
            .filtered(lambda p: (p.create_date.date() - datetime.date.today()).days > 7)
        )
        _logger.info(msg=f"Archived and removed {old_sale_orders} orders.")
