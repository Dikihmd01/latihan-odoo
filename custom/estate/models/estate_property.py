from ast import Lambda
from copy import copy
from email.policy import default
from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postocde = fields.Char(string='Post Code')
    date_availability = fields.Date(string='Date Availability', default=lambda self: fields.Datetime.today(), copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='state', default='new', required=True, copy=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
