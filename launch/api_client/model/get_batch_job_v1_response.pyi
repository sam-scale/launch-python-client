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

class GetBatchJobV1Response(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "duration",
            "status",
        }

        class properties:
            duration = schemas.NumberSchema

            @staticmethod
            def status() -> typing.Type["BatchJobStatus"]:
                return BatchJobStatus
            num_tasks_completed = schemas.IntSchema
            num_tasks_pending = schemas.IntSchema
            result = schemas.StrSchema
            __annotations__ = {
                "duration": duration,
                "status": status,
                "num_tasks_completed": num_tasks_completed,
                "num_tasks_pending": num_tasks_pending,
                "result": result,
            }
    duration: MetaOapg.properties.duration
    status: "BatchJobStatus"

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> "BatchJobStatus": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["num_tasks_completed"]
    ) -> MetaOapg.properties.num_tasks_completed: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["num_tasks_pending"]
    ) -> MetaOapg.properties.num_tasks_pending: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "duration",
                "status",
                "num_tasks_completed",
                "num_tasks_pending",
                "result",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> "BatchJobStatus": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["num_tasks_completed"]
    ) -> typing.Union[MetaOapg.properties.num_tasks_completed, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["num_tasks_pending"]
    ) -> typing.Union[MetaOapg.properties.num_tasks_pending, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["result"]
    ) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "duration",
                "status",
                "num_tasks_completed",
                "num_tasks_pending",
                "result",
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
        duration: typing.Union[
            MetaOapg.properties.duration,
            decimal.Decimal,
            int,
            float,
        ],
        status: "BatchJobStatus",
        num_tasks_completed: typing.Union[
            MetaOapg.properties.num_tasks_completed, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        num_tasks_pending: typing.Union[
            MetaOapg.properties.num_tasks_pending, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        result: typing.Union[MetaOapg.properties.result, str, schemas.Unset] = schemas.unset,
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
    ) -> "GetBatchJobV1Response":
        return super().__new__(
            cls,
            *_args,
            duration=duration,
            status=status,
            num_tasks_completed=num_tasks_completed,
            num_tasks_pending=num_tasks_pending,
            result=result,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.batch_job_status import BatchJobStatus
