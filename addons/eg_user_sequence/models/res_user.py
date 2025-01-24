from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    code = fields.Char(string='Code')

    @api.model
    def create(self, vals):
        res = super(ResUsers, self).create(vals)
        for rec in res:
            code = self.env['ir.sequence'].next_by_code(
                'res.users')
            rec.code = code
        return res
