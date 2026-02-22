from odoo import models, fields

class Empresa(models.Model):
    # DELEGATION INHERITANCE: delegates to Workplace via FK
    _name = 'module3.empresa'
    _description = 'Empresa'
    _inherits = {
        'module1.workplace': 'workplace_id',
    }

    workplace_id = fields.Many2one(
        comodel_name='module1.workplace',
        string='Workplace',
        required=True,
        ondelete='cascade',
        auto_join=True,
    )

    tax_id = fields.Char(string='Tax ID / CIF')
    industry = fields.Char(string='Industry')