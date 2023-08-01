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

class PytorchFramework(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the entity-layer class for a Pytorch framework specification.
    """

    class MetaOapg:
        required = {
            "pytorch_image_tag",
            "framework_type",
        }

        class properties:
            class framework_type(schemas.EnumBase, schemas.StrSchema):
                @schemas.classproperty
                def PYTORCH(cls):
                    return cls("pytorch")
            pytorch_image_tag = schemas.StrSchema
            __annotations__ = {
                "framework_type": framework_type,
                "pytorch_image_tag": pytorch_image_tag,
            }
    pytorch_image_tag: MetaOapg.properties.pytorch_image_tag
    framework_type: MetaOapg.properties.framework_type

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["framework_type"]
    ) -> MetaOapg.properties.framework_type: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["pytorch_image_tag"]
    ) -> MetaOapg.properties.pytorch_image_tag: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "framework_type",
                "pytorch_image_tag",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["framework_type"]
    ) -> MetaOapg.properties.framework_type: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["pytorch_image_tag"]
    ) -> MetaOapg.properties.pytorch_image_tag: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "framework_type",
                "pytorch_image_tag",
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
        pytorch_image_tag: typing.Union[
            MetaOapg.properties.pytorch_image_tag,
            str,
        ],
        framework_type: typing.Union[
            MetaOapg.properties.framework_type,
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
    ) -> "PytorchFramework":
        return super().__new__(
            cls,
            *_args,
            pytorch_image_tag=pytorch_image_tag,
            framework_type=framework_type,
            _configuration=_configuration,
            **kwargs,
        )
