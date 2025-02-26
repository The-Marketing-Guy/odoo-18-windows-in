from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Many2one(comodel_name='res.partner', string="Vendor")
