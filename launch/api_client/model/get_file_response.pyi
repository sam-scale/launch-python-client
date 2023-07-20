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

class GetFileResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "filename",
            "size",
            "id",
        }

        class properties:
            filename = schemas.StrSchema
            id = schemas.StrSchema
            size = schemas.IntSchema
            __annotations__ = {
                "filename": filename,
                "id": id,
                "size": size,
            }
    filename: MetaOapg.properties.filename
    size: MetaOapg.properties.size
    id: MetaOapg.properties.id

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "filename",
                "id",
                "size",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "filename",
                "id",
                "size",
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
        filename: typing.Union[
            MetaOapg.properties.filename,
            str,
        ],
        size: typing.Union[
            MetaOapg.properties.size,
            decimal.Decimal,
            int,
        ],
        id: typing.Union[
            MetaOapg.properties.id,
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
    ) -> "GetFileResponse":
        return super().__new__(
            cls,
            *_args,
            filename=filename,
            size=size,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
