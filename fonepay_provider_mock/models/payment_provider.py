from odoo import fields, models
import requests

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('fonepay', 'Fonepay')],
        ondelete={'fonepay': 'set default'},
    )
    fonepay_api_url = fields.Char(string='Fonepay API URL', default='http://127.0.0.1:5000')
    fonepay_merchant_code = fields.Char(string='Merchant Code',groups='base.group_system')
    fonepay_username = fields.Char(string='Username',groups='base.group_system')
    fonepay_password = fields.Char(string='Password',groups='base.group_system')
    fonepay_secret_key = fields.Char(string='Secret Key',groups='base.group_system')
    fonepay_test_mode = fields.Boolean(string='Sandbox Mode', groups='base.group_system')

    def _is_available(self, *args, **kwargs):
        if self.filtered(lambda p: p.code == 'fonepay'):
            return True
        return super()._is_available(*args, **kwargs)

    def fonepay_test_connection(self):
        self.ensure_one()

        if self.code != 'fonepay':
            return

        try:
            response = requests.post(
                url=f'{self.fonepay_api_url}/auth',
                json={
                    "username": self.fonepay_username,
                    "password": self.fonepay_password,
                },
                timeout=20,
            )
            if response.status_code == 200:
                return{
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Fonepay',
                        'message': 'Connected to fonepay successfully',
                        'type': 'success',
                        'sticky': False,
                        'next': {'type': 'ir.actions.act_window_close'},
                    }
                }
            return{
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Fonepay',
                    'message': f'Connection failed ({response.status_code})',
                    'type': 'warning',
                    'sticky': False,
                    'next': {'type': 'ir.actions.act_window_close'},
                },
            }
        except Exception as e:
            return{
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Fonepay',
                    'message': str(e),
                    'sticky': True,
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }
