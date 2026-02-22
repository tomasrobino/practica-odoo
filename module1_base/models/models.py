# from odoo import models, fields, api


# class module1_base(models.Model):
#     _name = 'module1_base.module1_base'
#     _description = 'module1_base.module1_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

