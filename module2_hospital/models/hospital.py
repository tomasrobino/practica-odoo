from odoo import models, fields

class Hospital(models.Model):
    # DELEGATION INHERITANCE: delegates to Workplace and SleepPlace via FK
    _name = 'module2.hospital'
    _description = 'Hospital'
    _inherits = {
        'module1.workplace': 'workplace_id',
        'module1.sleepplace': 'sleepplace_id',
    }

    workplace_id = fields.Many2one(
        comodel_name='module1.workplace',
        string='Workplace',
        required=True,
        ondelete='cascade',
        auto_join=True,
    )
    sleepplace_id = fields.Many2one(
        comodel_name='module1.sleepplace',
        string='Sleep Place',
        required=True,
        ondelete='cascade',
        auto_join=True,
    )

    speciality = fields.Char(string='Speciality')
    emergency_phone = fields.Char(string='Emergency Phone')