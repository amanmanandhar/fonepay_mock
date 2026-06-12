from odoo import fields, models

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('fonepay', 'Fonepay')],
        ondelete={'fonepay': 'set default'},
    )

    def _is_available(self, *args, **kwargs):
        if self.filtered(lambda p: p.code == 'fonepay'):
            return True
        return super()._is_available(*args, **kwargs)