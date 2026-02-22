from odoo import models, fields

class Empleado(models.Model):
    # PROTOTYPE INHERITANCE: copies Persona's fields into a NEW independent model/table
    _name = 'module3.empleado'
    _description = 'Empleado'
    _inherit = 'module1.persona'

    position = fields.Char(string='Position')
    salary = fields.Float(string='Salary')
    hire_date = fields.Date(string='Hire Date')
    empresa_id = fields.Many2one(
        comodel_name='module3.empresa',
        string='Empresa',
    )