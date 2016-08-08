# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobCollectionDefinition(Model):
    """JobCollectionDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the job collection resource identifier.
    :vartype id: str
    :ivar type: Gets the job collection resource type.
    :vartype type: str
    :param name: Gets or sets the job collection resource name.
    :type name: str
    :param location: Gets or sets the storage account location.
    :type location: str
    :param tags: Gets or sets the tags.
    :type tags: dict
    :param properties: Gets or sets the job collection properties.
    :type properties: :class:`JobCollectionProperties
     <azure.mgmt.scheduler.models.JobCollectionProperties>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'JobCollectionProperties'},
    }

    def __init__(self, name=None, location=None, tags=None, properties=None):
        self.id = None
        self.type = None
        self.name = name
        self.location = location
        self.tags = tags
        self.properties = properties