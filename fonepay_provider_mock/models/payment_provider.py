from odoo import fields, models

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('fonepay', 'Fonepay')],
        ondelete={'fonepay': 'set default'},
    )

    fonepay_merchant_code = fields.Char(string='Merchant Code',groups='base.group_system')
    fonepay_username = fields.Char(string='Username',groups='base.group_system')
    fonepay_password = fields.Char(string='Password',groups='base.group_system')
    fonepay_secret_key = fields.Char(string='Secret Key',groups='base.group_system')
    fonepay_test_mode = fields.Boolean(string='Sandbox Mode', groups='base.group_system')

    def _is_available(self, *args, **kwargs):
        if self.filtered(lambda p: p.code == 'fonepay'):
            return True
        return super()._is_available(*args, **kwargs)