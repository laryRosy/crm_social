# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCRMSocial(TransactionCase):

    def setUp(self):
        super(TestCRMSocial, self).setUp()
        self.customer = self.env.ref("base.partner_admin")
        self.customer.social_facebook = "test@facebook.com"
        self.customer.social_twitter = "test@twitter.com"
        self.customer.social_linkedin = None

    def test_profile_incomplete(self):
        self.assertTrue(self.customer.profile_incomplete)

    def test_profile_complete(self):
        self.customer.social_linkedin = "test@linkedin.com"
        self.assertFalse(self.customer.profile_incomplete)

