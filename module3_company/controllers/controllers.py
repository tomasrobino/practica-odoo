# from odoo import http


# class Module3Company(http.Controller):
#     @http.route('/module3_company/module3_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module3_company/module3_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module3_company.listing', {
#             'root': '/module3_company/module3_company',
#             'objects': http.request.env['module3_company.module3_company'].search([]),
#         })

#     @http.route('/module3_company/module3_company/objects/<model("module3_company.module3_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module3_company.object', {
#             'object': obj
#         })

