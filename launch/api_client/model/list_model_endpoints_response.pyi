# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
from launch_client import schemas  # noqa: F401

class ListModelEndpointsResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "model_endpoints",
        }

        class properties:
            class model_endpoints(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["GetModelEndpointResponse"]:
                        return GetModelEndpointResponse
                def __new__(
                    cls,
                    arg: typing.Union[
                        typing.Tuple["GetModelEndpointResponse"],
                        typing.List["GetModelEndpointResponse"],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "model_endpoints":
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "GetModelEndpointResponse":
                    return super().__getitem__(i)
            __annotations__ = {
                "model_endpoints": model_endpoints,
            }
    model_endpoints: MetaOapg.properties.model_endpoints

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_endpoints"]
    ) -> MetaOapg.properties.model_endpoints: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "model_endpoints",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_endpoints"]
    ) -> MetaOapg.properties.model_endpoints: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "model_endpoints",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        model_endpoints: typing.Union[
            MetaOapg.properties.model_endpoints,
            list,
            tuple,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "ListModelEndpointsResponse":
        return super().__new__(
            cls,
            *args,
            model_endpoints=model_endpoints,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.get_model_endpoint_response import (
    GetModelEndpointResponse,
)
