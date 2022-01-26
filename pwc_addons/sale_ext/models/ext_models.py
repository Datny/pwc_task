import logging


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOlder(models.Model):
    _inherit = ["sale.order.line"]
    conv_factor = fields.Integer(default=1)
    customer_quantity = fields.Float(compute="_compute_customer_quantity", store=True)

    @api.depends("conv_factor", "product_uom_qty")
    def _compute_customer_quantity(self):
        for rec in self:
            rec.customer_quantity = rec.conv_factor * rec.product_uom_qty

    @api.constrains("conv_factor")
    def _verify_conv_factor(self):
        for rec in self:
            if rec.conv_factor <= 0:
                raise ValidationError(_("Conv Factor cannot be smaller or equal 0"))

    @api.onchange("conv_factor")
    def _onchange_conv_factor(self):
        if self.conv_factor <= 0:
            self.conv_factor = 1
