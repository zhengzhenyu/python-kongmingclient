#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from kongmingclient.common import http
from kongmingclient.v1 import hosts
from kongmingclient.v1 import instance_cpu_mappings
from kongmingclient.v1 import instances


class Client(object):
    """Client for the KongMing v1 API."""

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the KongMing v1 API."""
        self.http_client = http._construct_http_client(*args, **kwargs)

        self.instance_cpu_mappings = \
            instance_cpu_mappings.InstanceCPUMapingManager(self.http_client)

        self.instances = \
            instances.InstanceManager(self.http_client)

        self.hosts = \
            hosts.HostManager(self.http_client)
