from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_customer = fields.Boolean(string="Is Customer")
    is_vendor = fields.Boolean(string="Is Vendor")
