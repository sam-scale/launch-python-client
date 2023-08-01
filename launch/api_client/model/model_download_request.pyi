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

class ModelDownloadRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "model_name",
            "format",
        }

        class properties:
            format = schemas.StrSchema
            model_name = schemas.StrSchema
            __annotations__ = {
                "format": format,
                "model_name": model_name,
            }
    model_name: MetaOapg.properties.model_name
    format: MetaOapg.properties.format

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_name"]) -> MetaOapg.properties.model_name: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "format",
                "model_name",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_name"]) -> MetaOapg.properties.model_name: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "format",
                "model_name",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        model_name: typing.Union[
            MetaOapg.properties.model_name,
            str,
        ],
        format: typing.Union[
            MetaOapg.properties.format,
            str,
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
    ) -> "ModelDownloadRequest":
        return super().__new__(
            cls,
            *_args,
            model_name=model_name,
            format=format,
            _configuration=_configuration,
            **kwargs,
        )
