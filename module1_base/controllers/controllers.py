# from odoo import http


# class Module1Base(http.Controller):
#     @http.route('/module1_base/module1_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module1_base/module1_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module1_base.listing', {
#             'root': '/module1_base/module1_base',
#             'objects': http.request.env['module1_base.module1_base'].search([]),
#         })

#     @http.route('/module1_base/module1_base/objects/<model("module1_base.module1_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module1_base.object', {
#             'object': obj
#         })

