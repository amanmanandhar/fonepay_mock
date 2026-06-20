# -*- coding: utf-8 -*-
# from odoo import http


# class FonepayIntegrationMock(http.Controller):
#     @http.route('/fonepay_integration_mock/fonepay_integration_mock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fonepay_integration_mock/fonepay_integration_mock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fonepay_integration_mock.listing', {
#             'root': '/fonepay_integration_mock/fonepay_integration_mock',
#             'objects': http.request.env['fonepay_integration_mock.fonepay_integration_mock'].search([]),
#         })

#     @http.route('/fonepay_integration_mock/fonepay_integration_mock/objects/<model("fonepay_integration_mock.fonepay_integration_mock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fonepay_integration_mock.object', {
#             'object': obj
#         })

