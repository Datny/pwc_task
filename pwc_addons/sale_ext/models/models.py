# -*- coding: utf-8 -*-
import datetime
import logging

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
        """Creates new (sale.order.archive) object for orders (sale.order) older than 7 days  and delete (sale.order)
        which have been archived"""
        _logger = logging.getLogger(__name__)
        SaleOrder = self.env["sale.order"]
        SaleOlderArchive = self.env["sale.order.archive"]
        sale_orders_to_archive = []
        old_sale_orders = SaleOrder.search([]).filtered(
            lambda p: ((datetime.date.today() - p.create_date.date()).days > 7)
        )
        for order in old_sale_orders:
            sale_orders_to_archive.append(
                dict(
                    name=order.name,
                    customer=order.partner_id.id,
                    sale_person=order.user_id.id,
                    order_currency=order.currency_id.id,
                    order_total_amount=order.amount_total,
                    count_of_order_lines=len(order.order_line.ids),
                    create_date=order.create_date,
                )
            )
            super(models.Model, order).unlink()
        number_of_archived_orders = len(SaleOlderArchive.create(sale_orders_to_archive))
        _logger.info(msg=f"Archived and removed {number_of_archived_orders} orders.")
        return number_of_archived_orders
