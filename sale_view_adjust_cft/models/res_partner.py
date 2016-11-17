# -*- coding: utf-8 -*-
# Copyright 2016 Ecosoft Co. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class res_partner_rank(models.Model):
    _inherit = 'res.partner'

    customer_rank = fields.Many2one('res.partner.rank','Rank')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: