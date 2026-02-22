# from odoo import http


# class Module2Hospital(http.Controller):
#     @http.route('/module2_hospital/module2_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module2_hospital/module2_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module2_hospital.listing', {
#             'root': '/module2_hospital/module2_hospital',
#             'objects': http.request.env['module2_hospital.module2_hospital'].search([]),
#         })

#     @http.route('/module2_hospital/module2_hospital/objects/<model("module2_hospital.module2_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module2_hospital.object', {
#             'object': obj
#         })

