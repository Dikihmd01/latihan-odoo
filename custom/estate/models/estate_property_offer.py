from odoo import api, fields, models


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'This is property offers'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='status', copy=False)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Buyer', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', string='Property Name', required=True)
    
    
    
