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


class CloneModelBundleV2Request(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request object for cloning a Model Bundle from another one.
    """

    class MetaOapg:
        required = {
            "original_model_bundle_id",
        }

        class properties:
            original_model_bundle_id = schemas.StrSchema
            new_app_config = schemas.DictSchema
            __annotations__ = {
                "original_model_bundle_id": original_model_bundle_id,
                "new_app_config": new_app_config,
            }

    original_model_bundle_id: MetaOapg.properties.original_model_bundle_id

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["original_model_bundle_id"]
    ) -> MetaOapg.properties.original_model_bundle_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["new_app_config"]
    ) -> MetaOapg.properties.new_app_config:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "original_model_bundle_id",
                "new_app_config",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["original_model_bundle_id"]
    ) -> MetaOapg.properties.original_model_bundle_id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["new_app_config"]
    ) -> typing.Union[MetaOapg.properties.new_app_config, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "original_model_bundle_id",
                "new_app_config",
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
        original_model_bundle_id: typing.Union[
            MetaOapg.properties.original_model_bundle_id,
            str,
        ],
        new_app_config: typing.Union[
            MetaOapg.properties.new_app_config, dict, frozendict.frozendict, schemas.Unset
        ] = schemas.unset,
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
    ) -> "CloneModelBundleV2Request":
        return super().__new__(
            cls,
            *_args,
            original_model_bundle_id=original_model_bundle_id,
            new_app_config=new_app_config,
            _configuration=_configuration,
            **kwargs,
        )
