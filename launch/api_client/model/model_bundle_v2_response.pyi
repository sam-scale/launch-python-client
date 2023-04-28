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

class ModelBundleV2Response(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Response object for a single Model Bundle.
    """

    class MetaOapg:
        required = {
            "flavor",
            "metadata",
            "model_artifact_ids",
            "name",
            "created_at",
            "id",
        }

        class properties:
            created_at = schemas.DateTimeSchema

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
            id = schemas.StrSchema
            metadata = schemas.DictSchema

            class model_artifact_ids(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.StrSchema
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                        typing.List[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "model_artifact_ids":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            name = schemas.StrSchema
            schema_location = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "flavor": flavor,
                "id": id,
                "metadata": metadata,
                "model_artifact_ids": model_artifact_ids,
                "name": name,
                "schema_location": schema_location,
            }
    flavor: MetaOapg.properties.flavor
    metadata: MetaOapg.properties.metadata
    model_artifact_ids: MetaOapg.properties.model_artifact_ids
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flavor"]) -> MetaOapg.properties.flavor: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_artifact_ids"]
    ) -> MetaOapg.properties.model_artifact_ids: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> MetaOapg.properties.schema_location: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "flavor",
                "id",
                "metadata",
                "model_artifact_ids",
                "name",
                "schema_location",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flavor"]) -> MetaOapg.properties.flavor: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_artifact_ids"]
    ) -> MetaOapg.properties.model_artifact_ids: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> typing.Union[MetaOapg.properties.schema_location, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "flavor",
                "id",
                "metadata",
                "model_artifact_ids",
                "name",
                "schema_location",
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
        metadata: typing.Union[
            MetaOapg.properties.metadata,
            dict,
            frozendict.frozendict,
        ],
        model_artifact_ids: typing.Union[
            MetaOapg.properties.model_artifact_ids,
            list,
            tuple,
        ],
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        created_at: typing.Union[
            MetaOapg.properties.created_at,
            str,
            datetime,
        ],
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        schema_location: typing.Union[MetaOapg.properties.schema_location, str, schemas.Unset] = schemas.unset,
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
    ) -> "ModelBundleV2Response":
        return super().__new__(
            cls,
            *_args,
            flavor=flavor,
            metadata=metadata,
            model_artifact_ids=model_artifact_ids,
            name=name,
            created_at=created_at,
            id=id,
            schema_location=schema_location,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.cloudpickle_artifact_flavor import (
    CloudpickleArtifactFlavor,
)
from launch_client.model.runnable_image_flavor import RunnableImageFlavor
from launch_client.model.triton_enhanced_runnable_image_flavor import (
    TritonEnhancedRunnableImageFlavor,
)
from launch_client.model.zip_artifact_flavor import ZipArtifactFlavor
