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

class CreateModelBundleV2Request(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request object for creating a Model Bundle.
    """

    class MetaOapg:
        required = {
            "flavor",
            "name",
            "schema_location",
        }

        class properties:
            class flavor(
                schemas.ComposedSchema,
            ):
                class MetaOapg:
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            CloudpickleArtifactFlavor,
                            ZipArtifactFlavor,
                            RunnableImageFlavor,
                            StreamingEnhancedRunnableImageFlavor,
                            TritonEnhancedRunnableImageFlavor,
                        ]
                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                        str,
                        date,
                        datetime,
                        uuid.UUID,
                        int,
                        float,
                        decimal.Decimal,
                        bool,
                        None,
                        list,
                        tuple,
                        bytes,
                        io.FileIO,
                        io.BufferedReader,
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
                ) -> "flavor":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            name = schemas.StrSchema
            schema_location = schemas.StrSchema
            metadata = schemas.DictSchema
            __annotations__ = {
                "flavor": flavor,
                "name": name,
                "schema_location": schema_location,
                "metadata": metadata,
            }
    flavor: MetaOapg.properties.flavor
    name: MetaOapg.properties.name
    schema_location: MetaOapg.properties.schema_location

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flavor"]) -> MetaOapg.properties.flavor: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> MetaOapg.properties.schema_location: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "flavor",
                "name",
                "schema_location",
                "metadata",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flavor"]) -> MetaOapg.properties.flavor: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> MetaOapg.properties.schema_location: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["metadata"]
    ) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "flavor",
                "name",
                "schema_location",
                "metadata",
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
        flavor: typing.Union[
            MetaOapg.properties.flavor,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader,
        ],
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        schema_location: typing.Union[
            MetaOapg.properties.schema_location,
            str,
        ],
        metadata: typing.Union[
            MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset
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
    ) -> "CreateModelBundleV2Request":
        return super().__new__(
            cls,
            *_args,
            flavor=flavor,
            name=name,
            schema_location=schema_location,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.cloudpickle_artifact_flavor import CloudpickleArtifactFlavor
from launch_client.model.runnable_image_flavor import RunnableImageFlavor
from launch_client.model.streaming_enhanced_runnable_image_flavor import (
    StreamingEnhancedRunnableImageFlavor,
)
from launch_client.model.triton_enhanced_runnable_image_flavor import (
    TritonEnhancedRunnableImageFlavor,
)
from launch_client.model.zip_artifact_flavor import ZipArtifactFlavor
