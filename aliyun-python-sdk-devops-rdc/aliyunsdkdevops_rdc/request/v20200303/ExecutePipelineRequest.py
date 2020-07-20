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

from aliyunsdkcore.request import RpcRequest

class ExecutePipelineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'ExecutePipeline')
		self.set_method('POST')

	def get_Parameters(self):
		return self.get_body_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_body_params('Parameters', Parameters)

	def get_UserPk(self):
		return self.get_body_params().get('UserPk')

	def set_UserPk(self,UserPk):
		self.add_body_params('UserPk', UserPk)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_PipelineId(self):
		return self.get_body_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_body_params('PipelineId', PipelineId)