from odoo.tests import common
from odoo.exceptions import ValidationError


class TestModelExtensionSaleOrder(common.TransactionCase):
    def test_verify_conv_factor(self):
        so_1 = self.env.ref("sale.sale_order_line_1")

        with self.assertRaises(ValidationError):
            so_1.conv_factor = 0
        with self.assertRaises(ValidationError):
            so_1.conv_factor = -1

        so_1.conv_factor = 4
        self.assertEqual(so_1.conv_factor, 4)

    def test_compute_customer_quantity(self):
        so_1 = self.env.ref("sale.sale_order_line_1")
        self.assertEqual(so_1.conv_factor, 1)
        self.assertEqual(
            so_1.customer_quantity, so_1.conv_factor * so_1.product_uom_qty
        )

        so_1.conv_factor = 2
        self.assertEqual(
            so_1.customer_quantity, so_1.conv_factor * so_1.product_uom_qty
        )

        so_1.product_uom_qty = 4
        self.assertEqual(
            so_1.customer_quantity, so_1.conv_factor * so_1.product_uom_qty
        )
