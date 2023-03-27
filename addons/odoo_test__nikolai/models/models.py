import random
from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test_field = fields.Char(string='Test', readonly=False, states={'draft': [('readonly', False)]})

    def _compute_test_field(self, from_create_or_write=False):
        for order in self:
            if from_create_or_write:
                continue
            if order.state == 'draft':
                order.test_field = str(random.randint(1, 100))
            else:
                order.test_field = f"{order.amount_total} - {order.date_order.strftime('%m/%d/%Y %H:%M:%S')}"

    @api.model_create_multi
    def create(self, vals_list):
        orders = super(SaleOrder, self).create(vals_list)
        orders._compute_test_field(from_create_or_write=True)
        return orders

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        self._compute_test_field(from_create_or_write=True)
        return res

    @api.constrains('test_field')
    def _check_test_field_length(self):
        for order in self:
            if len(order.test_field) > 50:
                raise ValidationError('The text length must be less than 50 characters!')
