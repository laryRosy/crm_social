# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    social_twitter = fields.Char('Twitter Account')
    social_facebook = fields.Char('Facebook Account', group_operator='bool_and')
    social_linkedin = fields.Char('LinkedIn Account')

    profile_incomplete = fields.Boolean('Profile Incomplete', compute='_compute_profile_incomplete', store=True)

    @api.depends('social_twitter', 'social_facebook', 'social_linkedin')
    def _compute_profile_incomplete(self):
        for customer in self:
            if customer.social_facebook and customer.social_twitter and customer.social_linkedin:
                customer.profile_incomplete = False
            else:
                customer.profile_incomplete = True
