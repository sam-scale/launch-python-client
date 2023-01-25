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

from launch.api_client import schemas  # noqa: F401


class ModelBundleResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Response object for a single Model Bundle.
    """

    class MetaOapg:
        required = {
            "metadata",
            "requirements",
            "model_artifact_ids",
            "packaging_type",
            "name",
            "created_at",
            "location",
            "id",
            "env_params",
        }

        class properties:
            created_at = schemas.DateTimeSchema

            @staticmethod
            def env_params() -> typing.Type["ModelBundleEnvironmentParams"]:
                return ModelBundleEnvironmentParams

            id = schemas.StrSchema
            location = schemas.StrSchema
            metadata = schemas.DictSchema

            class model_artifact_ids(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.StrSchema

                def __new__(
                    cls,
                    arg: typing.Union[
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
                    _configuration: typing.Optional[
                        schemas.Configuration
                    ] = None,
                ) -> "model_artifact_ids":
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            name = schemas.StrSchema

            @staticmethod
            def packaging_type() -> typing.Type["ModelBundlePackagingType"]:
                return ModelBundlePackagingType

            class requirements(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.StrSchema

                def __new__(
                    cls,
                    arg: typing.Union[
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
                    _configuration: typing.Optional[
                        schemas.Configuration
                    ] = None,
                ) -> "requirements":
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            app_config = schemas.DictSchema
            schema_location = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "env_params": env_params,
                "id": id,
                "location": location,
                "metadata": metadata,
                "model_artifact_ids": model_artifact_ids,
                "name": name,
                "packaging_type": packaging_type,
                "requirements": requirements,
                "app_config": app_config,
                "schema_location": schema_location,
            }

    metadata: MetaOapg.properties.metadata
    requirements: MetaOapg.properties.requirements
    model_artifact_ids: MetaOapg.properties.model_artifact_ids
    packaging_type: "ModelBundlePackagingType"
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at
    location: MetaOapg.properties.location
    id: MetaOapg.properties.id
    env_params: "ModelBundleEnvironmentParams"

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["env_params"]
    ) -> "ModelBundleEnvironmentParams":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["location"]
    ) -> MetaOapg.properties.location:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["metadata"]
    ) -> MetaOapg.properties.metadata:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_artifact_ids"]
    ) -> MetaOapg.properties.model_artifact_ids:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["packaging_type"]
    ) -> "ModelBundlePackagingType":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["requirements"]
    ) -> MetaOapg.properties.requirements:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["app_config"]
    ) -> MetaOapg.properties.app_config:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> MetaOapg.properties.schema_location:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "env_params",
                "id",
                "location",
                "metadata",
                "model_artifact_ids",
                "name",
                "packaging_type",
                "requirements",
                "app_config",
                "schema_location",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["env_params"]
    ) -> "ModelBundleEnvironmentParams":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["location"]
    ) -> MetaOapg.properties.location:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["metadata"]
    ) -> MetaOapg.properties.metadata:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_artifact_ids"]
    ) -> MetaOapg.properties.model_artifact_ids:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["packaging_type"]
    ) -> "ModelBundlePackagingType":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["requirements"]
    ) -> MetaOapg.properties.requirements:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["app_config"]
    ) -> typing.Union[MetaOapg.properties.app_config, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["schema_location"]
    ) -> typing.Union[MetaOapg.properties.schema_location, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "env_params",
                "id",
                "location",
                "metadata",
                "model_artifact_ids",
                "name",
                "packaging_type",
                "requirements",
                "app_config",
                "schema_location",
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
        metadata: typing.Union[
            MetaOapg.properties.metadata,
            dict,
            frozendict.frozendict,
        ],
        requirements: typing.Union[
            MetaOapg.properties.requirements,
            list,
            tuple,
        ],
        model_artifact_ids: typing.Union[
            MetaOapg.properties.model_artifact_ids,
            list,
            tuple,
        ],
        packaging_type: "ModelBundlePackagingType",
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        created_at: typing.Union[
            MetaOapg.properties.created_at,
            str,
            datetime,
        ],
        location: typing.Union[
            MetaOapg.properties.location,
            str,
        ],
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        env_params: "ModelBundleEnvironmentParams",
        app_config: typing.Union[
            MetaOapg.properties.app_config,
            dict,
            frozendict.frozendict,
            schemas.Unset,
        ] = schemas.unset,
        schema_location: typing.Union[
            MetaOapg.properties.schema_location, str, schemas.Unset
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
    ) -> "ModelBundleResponse":
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            requirements=requirements,
            model_artifact_ids=model_artifact_ids,
            packaging_type=packaging_type,
            name=name,
            created_at=created_at,
            location=location,
            id=id,
            env_params=env_params,
            app_config=app_config,
            schema_location=schema_location,
            _configuration=_configuration,
            **kwargs,
        )


from launch.api_client.model.model_bundle_environment_params import (
    ModelBundleEnvironmentParams,
)
from launch.api_client.model.model_bundle_packaging_type import (
    ModelBundlePackagingType,
)
