# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing_extensions import Self

from launch.api_client.models.create_docker_image_batch_job_resource_requests import (
    CreateDockerImageBatchJobResourceRequests,
)


class CreateDockerImageBatchJobBundleV1Request(BaseModel):
    """
    CreateDockerImageBatchJobBundleV1Request
    """  # noqa: E501

    command: List[StrictStr]
    env: Optional[Dict[str, StrictStr]] = None
    image_repository: StrictStr
    image_tag: StrictStr
    mount_location: Optional[StrictStr] = None
    name: StrictStr
    public: Optional[StrictBool] = False
    resource_requests: Optional[CreateDockerImageBatchJobResourceRequests] = None
    __properties: ClassVar[List[str]] = [
        "command",
        "env",
        "image_repository",
        "image_tag",
        "mount_location",
        "name",
        "public",
        "resource_requests",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateDockerImageBatchJobBundleV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of resource_requests
        if self.resource_requests:
            _dict["resource_requests"] = self.resource_requests.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateDockerImageBatchJobBundleV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "env": obj.get("env"),
                "image_repository": obj.get("image_repository"),
                "image_tag": obj.get("image_tag"),
                "mount_location": obj.get("mount_location"),
                "name": obj.get("name"),
                "public": obj.get("public") if obj.get("public") is not None else False,
                "resource_requests": CreateDockerImageBatchJobResourceRequests.from_dict(obj["resource_requests"])
                if obj.get("resource_requests") is not None
                else None,
            }
        )
        return _obj