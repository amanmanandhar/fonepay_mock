# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fonepay_integration_mock(models.Model):
#     _name = 'fonepay_integration_mock.fonepay_integration_mock'
#     _description = 'fonepay_integration_mock.fonepay_integration_mock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

