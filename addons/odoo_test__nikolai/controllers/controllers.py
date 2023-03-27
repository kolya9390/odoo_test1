# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTestNikolai(http.Controller):
#     @http.route('/odoo_test__nikolai/odoo_test__nikolai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_test__nikolai/odoo_test__nikolai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_test__nikolai.listing', {
#             'root': '/odoo_test__nikolai/odoo_test__nikolai',
#             'objects': http.request.env['odoo_test__nikolai.odoo_test__nikolai'].search([]),
#         })

#     @http.route('/odoo_test__nikolai/odoo_test__nikolai/objects/<model("odoo_test__nikolai.odoo_test__nikolai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_test__nikolai.object', {
#             'object': obj
#         })
