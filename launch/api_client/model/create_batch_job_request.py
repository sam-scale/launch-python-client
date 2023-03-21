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


class CreateBatchJobRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "model_bundle_id",
            "resource_requests",
            "serialization_format",
            "input_path",
            "labels",
        }

        class properties:
            input_path = schemas.StrSchema

            class labels(schemas.DictSchema):
                class MetaOapg:
                    additional_properties = schemas.StrSchema

                def __getitem__(
                    self,
                    name: typing.Union[
                        str,
                    ],
                ) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)

                def get_item_oapg(
                    self,
                    name: typing.Union[
                        str,
                    ],
                ) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)

                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[
                        MetaOapg.additional_properties,
                        str,
                    ],
                ) -> "labels":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            model_bundle_id = schemas.StrSchema

            @staticmethod
            def resource_requests() -> typing.Type["CreateBatchJobResourceRequests"]:
                return CreateBatchJobResourceRequests

            @staticmethod
            def serialization_format() -> typing.Type["BatchJobSerializationFormat"]:
                return BatchJobSerializationFormat

            __annotations__ = {
                "input_path": input_path,
                "labels": labels,
                "model_bundle_id": model_bundle_id,
                "resource_requests": resource_requests,
                "serialization_format": serialization_format,
            }

    model_bundle_id: MetaOapg.properties.model_bundle_id
    resource_requests: "CreateBatchJobResourceRequests"
    serialization_format: "BatchJobSerializationFormat"
    input_path: MetaOapg.properties.input_path
    labels: MetaOapg.properties.labels

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["input_path"]
    ) -> MetaOapg.properties.input_path:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_bundle_id"]
    ) -> MetaOapg.properties.model_bundle_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["resource_requests"]
    ) -> "CreateBatchJobResourceRequests":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["serialization_format"]
    ) -> "BatchJobSerializationFormat":
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "input_path",
                "labels",
                "model_bundle_id",
                "resource_requests",
                "serialization_format",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["input_path"]
    ) -> MetaOapg.properties.input_path:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["labels"]
    ) -> MetaOapg.properties.labels:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_bundle_id"]
    ) -> MetaOapg.properties.model_bundle_id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["resource_requests"]
    ) -> "CreateBatchJobResourceRequests":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["serialization_format"]
    ) -> "BatchJobSerializationFormat":
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "input_path",
                "labels",
                "model_bundle_id",
                "resource_requests",
                "serialization_format",
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
        model_bundle_id: typing.Union[
            MetaOapg.properties.model_bundle_id,
            str,
        ],
        resource_requests: "CreateBatchJobResourceRequests",
        serialization_format: "BatchJobSerializationFormat",
        input_path: typing.Union[
            MetaOapg.properties.input_path,
            str,
        ],
        labels: typing.Union[
            MetaOapg.properties.labels,
            dict,
            frozendict.frozendict,
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
    ) -> "CreateBatchJobRequest":
        return super().__new__(
            cls,
            *_args,
            model_bundle_id=model_bundle_id,
            resource_requests=resource_requests,
            serialization_format=serialization_format,
            input_path=input_path,
            labels=labels,
            _configuration=_configuration,
            **kwargs,
        )


from launch.api_client.model.batch_job_serialization_format import BatchJobSerializationFormat
from launch.api_client.model.create_batch_job_resource_requests import CreateBatchJobResourceRequests
