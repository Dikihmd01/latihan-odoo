from odoo import api, fields, models


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Table of type of properties'

    name = fields.Char(string='Name', required=True)
    # estate_property_id = fields.Many2one(comodel_name='estate.property', string='Property Types')

    _sql_constraints = [
        ('check_unique_propery_type',
         'UNIQUE(name)',
         'The property type must be unique!')]
