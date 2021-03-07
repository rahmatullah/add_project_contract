# -*- coding: utf-8 -*-
# from odoo import http


# class AddProjectContract(http.Controller):
#     @http.route('/add_project_contract/add_project_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_project_contract/add_project_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_project_contract.listing', {
#             'root': '/add_project_contract/add_project_contract',
#             'objects': http.request.env['add_project_contract.add_project_contract'].search([]),
#         })

#     @http.route('/add_project_contract/add_project_contract/objects/<model("add_project_contract.add_project_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_project_contract.object', {
#             'object': obj
#         })
