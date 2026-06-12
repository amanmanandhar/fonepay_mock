# -*- coding: utf-8 -*-
# from odoo import http


# class FonepayProviderMock(http.Controller):
#     @http.route('/fonepay_provider_mock/fonepay_provider_mock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fonepay_provider_mock/fonepay_provider_mock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fonepay_provider_mock.listing', {
#             'root': '/fonepay_provider_mock/fonepay_provider_mock',
#             'objects': http.request.env['fonepay_provider_mock.fonepay_provider_mock'].search([]),
#         })

#     @http.route('/fonepay_provider_mock/fonepay_provider_mock/objects/<model("fonepay_provider_mock.fonepay_provider_mock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fonepay_provider_mock.object', {
#             'object': obj
#         })

