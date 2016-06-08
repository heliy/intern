﻿# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This example shows how to work with the Boss' groups.  The Remote
class methods that being with 'group_' perform group operations.
"""

from ndio.remote.boss.remote import Remote, LATEST_VERSION
from ndio.ndresource.boss.resource import *

rmt = Remote('example.cfg')

API_VER = LATEST_VERSION

# Turn off SSL cert verification.  This is necessary for interacting with
# developer instances of the Boss.
import requests
from requests import Session, HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
rmt.project_service.session_send_opts = { 'verify': False }
rmt.metadata_service.session_send_opts = { 'verify': False }
rmt.volume_service.session_send_opts = { 'verify': False }

# Note spaces are not allowed in group names.
grp_name = 'my_group'

# Boss user names still in flux.
user_name = 'bossadmin'

print('Creating group . . .')
try:
    rmt.group_create(grp_name)
except HTTPError as h:
    # Assume group already exists if an exception raised.
    print(h.response.content)

print('Get info about group . . .')
data = rmt.group_get(grp_name)
print(data)

print('Add user to group . . .')
rmt.group_add_user(grp_name, user_name)

print('Confirm user is member of group . . .')
if rmt.group_get(grp_name, user_name):
    print('Confirmed')
else:
    print('NOT a member of the group')

print('Remove user from group . . .')
rmt.group_delete(grp_name, user_name)

print('Confirm user is not a member of group . . .')
if rmt.group_get(grp_name, user_name):
    print('Still a member of the group; removal must have failed')
else:
    print('Confirmed')

print('Deleting group . . .')
rmt.group_delete(grp_name)