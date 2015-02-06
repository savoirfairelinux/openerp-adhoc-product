# -*- encoding: utf-8 -*-
#
# OpenERP, Open Source Management Solution
# This module copyright (C) 2013 Savoir-faire Linux
# (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.tests import common


class TestCalculateProductVolume(common.TransactionCase):
    def setUp(self):
        super(TestCalculateProductVolume, self).setUp()
        self.product_model = self.env['product.product']
        self.product_uom = self.env['product.uom']

    def testCalculateVolume(self):
        product = self.product_model.create(
            {'name': 'p_name'}
        )

        uom = self.product_uom.search([('name', '=', 'm')])
        volume_dict = product.onchange_calculate_volume(2, 3, 4, uom.id)
        volume = volume_dict['value']['volume']
        self.assertEqual(volume, 24)

        volume_dict = product.onchange_calculate_volume(2, 3, 4, None)
        volume = volume_dict['value']['volume']
        self.assertEqual(volume, False)

        volume_dict = product.onchange_calculate_volume(2, 3, None, uom.id)
        volume = volume_dict['value']['volume']
        self.assertEqual(volume, False)

        volume_dict = product.onchange_calculate_volume(2.2, 3, 5.67, uom.id)
        volume = volume_dict['value']['volume']
        self.assertAlmostEqual(volume, 37.422)
