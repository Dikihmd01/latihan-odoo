from odoo import api, fields, models


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'This is property tags'

    name = fields.Char(string='Nama Tag')
