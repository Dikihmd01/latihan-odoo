from odoo import api, fields, models


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'This is property tags'

    name = fields.Char(string='Nama Tag')

    _sql_constraints = [
        ('check_unique_tag', 'UNIQUE(name)', 'The tag must be unique!')
    ]
