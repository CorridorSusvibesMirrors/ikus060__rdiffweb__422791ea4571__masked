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
Created on Apr 10, 2016

@author: Patrik Dufresne <patrik@ikus-soft.com>
"""

import os
from time import sleep
from unittest.case import skipIf

from parameterized import parameterized

import rdiffweb.test
from rdiffweb.core.librdiff import rdiff_backup_version
from rdiffweb.core.store import MAINTAINER_ROLE, USER_ROLE

RDIFF_BACKUP_VERSION = rdiff_backup_version()


class DeleteRepoTest(rdiffweb.test.WebCase):

    login = True

    def _delete(self, user, repo, confirm, redirect=None):
        body = {}
        if confirm is not None:
            body.update({'confirm': confirm})
        if redirect is not None:
            body['redirect'] = redirect
        self.getPage("/delete/" + user + "/" + repo + "/", method="POST", body=body)




    def test_delete_repo_wrong_confirm(self):
        """
        Check failure to delete a repo with wrong confirmation.
        """
        # Check initial list of repo
        self.assertEqual(['broker-repo', 'testcases'], [r.name for r in self.app.store.get_user('admin').repo_objs])
        # Delete repo with wrong confirmation.
        self._delete(self.USERNAME, self.REPO, 'wrong')
        # TODO Make sure the repository is not delete
        self.assertStatus(400)
        self.assertEqual(['broker-repo', 'testcases'], [r.name for r in self.app.store.get_user('admin').repo_objs])

    def test_delete_repo_without_confirm(self):
        """
        Check failure to delete a repo with wrong confirmation.
        """
        # Check initial list of repo
        self.assertEqual(['broker-repo', 'testcases'], [r.name for r in self.app.store.get_user('admin').repo_objs])
        # Delete repo without confirmation.
        self._delete(self.USERNAME, self.REPO, None)
        # Make sure the repository is not delete
        self.assertStatus(400)
        self.assertInBody('confirm: This field is required')
        self.assertEqual(['broker-repo', 'testcases'], [r.name for r in self.app.store.get_user('admin').repo_objs])




    def test_delete_repo_does_not_exists(self):
        # Given an invalid repo
        repo = 'invalid'
        # When trying to delete this repo
        self._delete(self.USERNAME, repo, repo)
        # Then a 404 is return to the user
        self.assertStatus(404)
