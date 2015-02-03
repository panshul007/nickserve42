#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import servicepackage.nameservice as nameservice

ns = nameservice.NameService()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello User, request something interesting!')


class AppStatus(webapp2.RequestHandler):
    def get(self):
        self.response.write('service alive')


class FetchRandomName(webapp2.RequestHandler):
    def get(self):
        self.response.write(ns.generaterandomname())


class FetchRandomIxName(webapp2.RequestHandler):
    def get(self):
        self.response.write(ns.generaterandomixname())

class FetchRandomAdjectiveForName(webapp2.RequestHandler):
    def get(self, name):
        self.response.write(ns.generate_random_adjective_for_name(name))

app = webapp2.WSGIApplication([
                                  ('/', MainHandler),
                                  ('/alive', AppStatus),
                                  ('/name', FetchRandomName),
                                  ('/ixname', FetchRandomIxName),
                                  webapp2.Route(r'/forname/<name>', handler=FetchRandomAdjectiveForName)
                              ], debug=True)
