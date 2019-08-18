# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class UpdateJvmConfigurationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateJvmConfiguration','edas')
		self.set_uri_pattern('/pop/v5/app/app_jvm_config')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MinHeapSize(self):
		return self.get_query_params().get('MinHeapSize')

	def set_MinHeapSize(self,MinHeapSize):
		self.add_query_param('MinHeapSize',MinHeapSize)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Options(self):
		return self.get_query_params().get('Options')

	def set_Options(self,Options):
		self.add_query_param('Options',Options)

	def get_MaxPermSize(self):
		return self.get_query_params().get('MaxPermSize')

	def set_MaxPermSize(self,MaxPermSize):
		self.add_query_param('MaxPermSize',MaxPermSize)

	def get_MaxHeapSize(self):
		return self.get_query_params().get('MaxHeapSize')

	def set_MaxHeapSize(self,MaxHeapSize):
		self.add_query_param('MaxHeapSize',MaxHeapSize)