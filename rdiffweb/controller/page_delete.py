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
'''
Created on Apr. 5, 2021

@author: Patrik Dufresne <patrik@ikus-soft.com>
'''
# Define the logger

import logging

import cherrypy
from wtforms import validators
from wtforms.fields.core import StringField

from rdiffweb.controller import Controller
from rdiffweb.controller.cherrypy_wtf import CherryForm
from rdiffweb.controller.dispatch import poppath
from rdiffweb.controller.filter_authorization import is_maintainer
from rdiffweb.core.librdiff import AccessDeniedError, DoesNotExistError
from rdiffweb.tools.i18n import ugettext as _

_logger = logging.getLogger(__name__)



