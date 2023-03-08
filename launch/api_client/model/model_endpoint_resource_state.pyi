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

class ModelEndpointResourceState(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the entity-layer class for the resource settings per worker of a Model Endpoint.
    """

    class MetaOapg:
        required = {
            "memory",
            "cpus",
            "gpus",
        }

        class properties:
            class cpus(
                schemas.ComposedSchema,
            ):
                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.IntSchema
                    any_of_2 = schemas.NumberSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            cls.any_of_2,
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
                ) -> "cpus":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class gpus(schemas.IntSchema):
                pass

            class memory(
                schemas.ComposedSchema,
            ):
                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.IntSchema
                    any_of_2 = schemas.NumberSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            cls.any_of_2,
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
                ) -> "memory":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            @staticmethod
            def gpu_type() -> typing.Type["GpuType"]:
                return GpuType
            optimize_costs = schemas.BoolSchema

            class storage(
                schemas.ComposedSchema,
            ):
                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.IntSchema
                    any_of_2 = schemas.NumberSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            cls.any_of_2,
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
                ) -> "storage":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "cpus": cpus,
                "gpus": gpus,
                "memory": memory,
                "gpu_type": gpu_type,
                "optimize_costs": optimize_costs,
                "storage": storage,
            }
    memory: MetaOapg.properties.memory
    cpus: MetaOapg.properties.cpus
    gpus: MetaOapg.properties.gpus

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpus"]) -> MetaOapg.properties.cpus: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpus"]) -> MetaOapg.properties.gpus: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpu_type"]) -> "GpuType": ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optimize_costs"]) -> MetaOapg.properties.optimize_costs: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> MetaOapg.properties.storage: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "cpus",
                "gpus",
                "memory",
                "gpu_type",
                "optimize_costs",
                "storage",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpus"]) -> MetaOapg.properties.cpus: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpus"]) -> MetaOapg.properties.gpus: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpu_type"]) -> typing.Union["GpuType", schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["optimize_costs"]
    ) -> typing.Union[MetaOapg.properties.optimize_costs, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["storage"]
    ) -> typing.Union[MetaOapg.properties.storage, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "cpus",
                "gpus",
                "memory",
                "gpu_type",
                "optimize_costs",
                "storage",
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
        memory: typing.Union[
            MetaOapg.properties.memory,
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
        cpus: typing.Union[
            MetaOapg.properties.cpus,
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
        gpus: typing.Union[
            MetaOapg.properties.gpus,
            decimal.Decimal,
            int,
        ],
        gpu_type: typing.Union["GpuType", schemas.Unset] = schemas.unset,
        optimize_costs: typing.Union[MetaOapg.properties.optimize_costs, bool, schemas.Unset] = schemas.unset,
        storage: typing.Union[
            MetaOapg.properties.storage,
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
            schemas.Unset,
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
    ) -> "ModelEndpointResourceState":
        return super().__new__(
            cls,
            *_args,
            memory=memory,
            cpus=cpus,
            gpus=gpus,
            gpu_type=gpu_type,
            optimize_costs=optimize_costs,
            storage=storage,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.gpu_type import GpuType
