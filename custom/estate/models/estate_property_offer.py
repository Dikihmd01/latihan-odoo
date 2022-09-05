from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'This is property offers'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='status',copy=False, help="Select Status")
    partner_id = fields.Many2one(comodel_name='res.partner', string='Buyer', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', string='Property Name', required=True)
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        string='Date Deadline',
        default=lambda self: fields.Datetime.today())
    
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for line in self:
            if line.create_date:
                line.date_deadline = line.create_date + timedelta(days=line.validity)
    
    def _inverse_date_deadline(self):
        for line in self:
            if line.date_deadline:
                line.validity = (line.date_deadline - line.create_date.date()).days
    
    def action_to_set_as_accepted(self):
        # for line in self:
        #     line.status = 'accepted'
        # return True
        if 'accepted' in self.mapped('property_id.offer_ids.status'):
            raise UserError('An offer has been accpedted!')
        self.write({'status': 'accepted'})

        return self.mapped('property_id').write({
            'state': 'offer accepted',
            'selling_price': self.price,
            'partner_id': self.partner_id.id
        })
    
    def action_to_set_as_refused(self):
        for line in self:
            line.status = 'refused'
        return True
