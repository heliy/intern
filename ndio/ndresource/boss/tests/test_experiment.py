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

import unittest
from ndio.ndresource.boss.resource import ExperimentResource

class TestExperimentResource(unittest.TestCase):
    def setUp(self):
        self.er = ExperimentResource('foo', 'bar', 'coords')

    def test_not_valid_volume(self):
        self.assertFalse(self.er.valid_volume())

    def test_get_route(self):
        self.assertEqual('{}/experiment/{}'.format(
            self.er.coll_name, self.er.name), self.er.get_route())

    def test_get_list_route(self):
        self.assertEqual(
            '{}/experiment/'.format(self.er.coll_name), 
            self.er.get_list_route())

    def test_hierarchy_method_setter(self):
        exp = 'iso'
        self.er.hierarchy_method = exp
        self.assertEqual(exp, self.er.hierarchy_method)

    def test_validate_hierarchy_method_near_iso(self):
        exp = 'near_iso'
        self.assertEqual(exp, self.er.validate_hierarchy_method(exp))

    def test_validate_hierarchy_method_iso(self):
        exp = 'iso'
        self.assertEqual(exp, self.er.validate_hierarchy_method(exp))

    def test_validate_hierarchy_method_slice(self):
        exp = 'slice'
        self.assertEqual(exp, self.er.validate_hierarchy_method(exp))

    def test_validate_hierarchy_method_bad(self):
        with self.assertRaises(ValueError):
            self.er.validate_hierarchy_method('foo')
