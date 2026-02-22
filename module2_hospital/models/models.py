# from odoo import models, fields, api


# class module2_hospital(models.Model):
#     _name = 'module2_hospital.module2_hospital'
#     _description = 'module2_hospital.module2_hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

