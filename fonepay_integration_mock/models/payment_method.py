from odoo import fields, models

class PosPaymentMethod(models.Model):
    _inherit="pos.payment.method"

    use_fonepay = fields.Boolean(string='Use Fonepay')

    fonepay_merchant_code = fields.Char(fields)
