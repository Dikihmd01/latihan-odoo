from ast import Lambda
from copy import copy
from email.policy import default
from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
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
    ], string='Garden Orientation', default="north")
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='state', default='new', required=True, copy=False)
    estate_property_id = fields.Many2one(comodel_name='estate.property.type', string='Property Types')
    user_id = fields.Many2one(comodel_name='res.users', string='Salesman')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Buyer')
    tag_ids = fields.Many2many(comodel_name='estate.property.tag', string='Tag')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offer')
    total_area = fields.Integer(compute='_compute_total_area', string='Total Area')
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for line in self:
            line.total_area = self.living_area + self.garden_area
    
    best_price = fields.Float(compute='_compute_best_price', string='Best Price')
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for line in self:
            line.best_price = max(line.mapped('offer_ids.price'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
