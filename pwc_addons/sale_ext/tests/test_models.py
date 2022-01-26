import datetime
from dateutil import relativedelta

from odoo.tests import common


class TestModelExtensionSaleOrder(common.TransactionCase):

    def test_cron_archive_and_remove_selected(self):
        so1, so2 = [self.env.ref(f"sale.sale_order_{el}") for el in range(1, 3)]
        number_of_all_sale_orders = self.env['sale.order'].search_count([])
        so1_id, so2_id = so1.id, so2.id
        so1.create_date = datetime.datetime.now() - datetime.timedelta(days=9)
        so2.create_date = datetime.datetime.now() - datetime.timedelta(days=8)

        archived_orders = self.env['sale.order.archive']._cron_archive_and_remove_selected()

        number_of_sale_orders_after_cron = self.env['sale.order'].search_count([])
        self.assertEqual(number_of_all_sale_orders, number_of_sale_orders_after_cron + archived_orders)
        self.assertEqual(bool(self.env['sale.order'].search([('id', '=', so1_id)])), False)
        self.assertEqual(bool(self.env['sale.order'].search([('id', '=', so2_id)])), False)