from odoo import models, fields

class Paciente(models.Model):
    # CLASS INHERITANCE: extends module1.persona in-place (same table, same _name)
    _inherit = 'module1.persona'

    medical_record = fields.Char(string='Medical Record Number')
    diagnosis = fields.Text(string='Diagnosis')
    admission_date = fields.Date(string='Admission Date')
    hospital_id = fields.Many2one(
        comodel_name='module2.hospital',
        string='Hospital',
    )