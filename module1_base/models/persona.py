from odoo import models, fields

class Persona(models.Model):
    _name = 'module1.persona'
    _description = 'Persona'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    workplace_id = fields.Many2one(
        comodel_name='module1.workplace',
        string='Workplace',
        ondelete='set null',
    )