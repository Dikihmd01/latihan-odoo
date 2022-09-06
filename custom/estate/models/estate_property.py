from ast import Try
from odoo import api, fields, models
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(
        string='Available From',
        default=lambda self: fields.Datetime.today(),
        copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(
        string='Selling Price',
        readonly=True,
        copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(
        string='Garden Area',
        onchange='_onchange_garden_area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation', default="north", onchange='_onchange_garden_area')
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='Status', default='new', required=True, copy=False)
    estate_property_id = fields.Many2one(
        comodel_name='estate.property.type',
        string='Property Types')
    user_id = fields.Many2one(comodel_name='res.users', string='Salesman')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Buyer')
    tag_ids = fields.Many2many(
        comodel_name='estate.property.tag',
        string='Tag')
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_id',
        string='Offer')
    total_area = fields.Integer(
        compute='_compute_total_area',
        string='Total Area',
        readonly=True)
    best_price = fields.Float(
        compute='_compute_best_price',
        string='Best Offer')

    _sql_constraints = [
        ('check_positive_expected_price',
         'CHECK(expected_price >= 0)',
         'The expected price must be a positive number!'),
        ('check_positive_selling_price',
         'CHECK(selling_price >= 0 OR selling_price = null)',
         'The selling price must be a positive number!'),
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for line in self:
            line.total_area = self.living_area + self.garden_area

    # def _inverse_total_area(self):
    #     for line in self:
    #         line.garden_area = line.total_area - line.living_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for line in self:
            try:
                line.best_price = max(line.offer_ids.mapped('price'))
            except ValueError:
                line.best_price = 0

    @api.onchange('garden')
    def _onchange_garden_area(self):
        for line in self:
            if line.garden:
                line.garden_area = 10
                line.garden_orientation = 'west'
            else:
                line.garden_area = 0
                line.garden_orientation = ''

    def action_to_set_state_to_sold(self):
        for line in self:
            if line.state == 'canceled':
                raise UserError('A canceled property cannot be sold')
            return self.write({'state': 'sold'})

    def action_to_set_state_to_canceled(self):
        for line in self:
            if line.state == 'sold':
                raise UserError('A sold property cannot be canceled')
            return self.write({'state': 'canceled'})
