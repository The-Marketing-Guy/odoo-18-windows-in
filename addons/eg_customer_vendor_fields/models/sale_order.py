from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Many2one(comodel_name='res.partner', string="Customer")
