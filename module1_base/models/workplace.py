from odoo import models, fields

class Workplace(models.Model):
    _name = 'module1.workplace'
    _description = 'Workplace'

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    capacity = fields.Integer(string='Capacity')