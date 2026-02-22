from odoo import models, fields

class SleepPlace(models.Model):
    _name = 'module1.sleepplace'
    _description = 'Sleep Place'

    name = fields.Char(string='Name', required=True)
    num_beds = fields.Integer(string='Number of Beds')
    floor = fields.Integer(string='Floor')