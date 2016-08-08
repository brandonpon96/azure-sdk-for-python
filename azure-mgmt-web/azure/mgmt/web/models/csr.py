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

from .resource import Resource


class Csr(Resource):
    """Certificate signing request object.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param csr_name: Name used to locate CSR object
    :type csr_name: str
    :param distinguished_name: Distinguished name of certificate to be created
    :type distinguished_name: str
    :param csr_string: Actual CSR string created
    :type csr_string: str
    :param pfx_blob: PFX certifcate of created certificate
    :type pfx_blob: str
    :param password: PFX password
    :type password: str
    :param public_key_hash: Hash of the certificates public key
    :type public_key_hash: str
    :param hosting_environment: Hosting environment
    :type hosting_environment: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'csr_name': {'key': 'properties.name', 'type': 'str'},
        'distinguished_name': {'key': 'properties.distinguishedName', 'type': 'str'},
        'csr_string': {'key': 'properties.csrString', 'type': 'str'},
        'pfx_blob': {'key': 'properties.pfxBlob', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'public_key_hash': {'key': 'properties.publicKeyHash', 'type': 'str'},
        'hosting_environment': {'key': 'properties.hostingEnvironment', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, csr_name=None, distinguished_name=None, csr_string=None, pfx_blob=None, password=None, public_key_hash=None, hosting_environment=None):
        super(Csr, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.csr_name = csr_name
        self.distinguished_name = distinguished_name
        self.csr_string = csr_string
        self.pfx_blob = pfx_blob
        self.password = password
        self.public_key_hash = public_key_hash
        self.hosting_environment = hosting_environment