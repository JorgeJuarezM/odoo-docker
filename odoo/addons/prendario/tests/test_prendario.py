# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.tests import HttpCase, tagged


@tagged('-at_install', 'post_install')
class PrendarioTestCase(HttpCase):
    """Basic unit test."""

    def test_initial_setup(self):
        """Basic test case."""
        self.assertTrue(True)