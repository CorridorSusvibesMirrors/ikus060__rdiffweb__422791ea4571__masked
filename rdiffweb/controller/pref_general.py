# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2012-2021 rdiffweb contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Default preference page to show general user information. It allows user
to change password ans refresh it's repository view.
"""

import logging
import re

import cherrypy
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Length, Regexp

from rdiffweb.controller import Controller, flash
from rdiffweb.controller.cherrypy_wtf import CherryForm
from rdiffweb.tools.i18n import ugettext as _

# Define the logger
_logger = logging.getLogger(__name__)

PATTERN_EMAIL = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')


class UserProfileForm(CherryForm):
    email = EmailField(_('Email'), validators=[DataRequired(), Regexp(PATTERN_EMAIL, message=_("Invalid email."))])





class PrefsGeneralPanelProvider(Controller):
    """
    Plugin to change user profile and password.
    """

    panel_id = 'general'

    panel_name = _('Profile')


