# -*- coding: utf-8  -*-
"""Family module for Wikimedia outreach wiki."""
from __future__ import unicode_literals

__version__ = '$Id$'

from pywikibot import family


# Outreach wiki custom family
class Family(family.WikimediaOrgFamily):

    """Family class for Wikimedia outreach wiki."""

    name = 'outreach'

    def __init__(self):
        """Constructor."""
        super(Family, self).__init__()

        self.interwiki_forward = 'wikipedia'
