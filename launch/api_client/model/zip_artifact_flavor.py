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


class ZipArtifactFlavor(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is the entity-layer class for the Model Bundle flavor of a zip artifact.
    """

    class MetaOapg:
        required = {
            "flavor",
            "requirements",
            "framework",
            "load_model_fn_module_path",
            "location",
            "load_predict_fn_module_path",
        }

        class properties:
            class flavor(schemas.EnumBase, schemas.StrSchema):
                class MetaOapg:
                    enum_value_to_name = {
                        "zip_artifact": "ZIP_ARTIFACT",
                    }

                @schemas.classproperty
                def ZIP_ARTIFACT(cls):
                    return cls("zip_artifact")

            class framework(
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
                            PytorchFramework,
                            TensorflowFramework,
                            CustomFramework,
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
                ) -> "framework":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            load_model_fn_module_path = schemas.StrSchema
            load_predict_fn_module_path = schemas.StrSchema
            location = schemas.StrSchema

            class requirements(schemas.ListSchema):
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
                ) -> "requirements":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            app_config = schemas.DictSchema
            __annotations__ = {
                "flavor": flavor,
                "framework": framework,
                "load_model_fn_module_path": load_model_fn_module_path,
                "load_predict_fn_module_path": load_predict_fn_module_path,
                "location": location,
                "requirements": requirements,
                "app_config": app_config,
            }

    flavor: MetaOapg.properties.flavor
    requirements: MetaOapg.properties.requirements
    framework: MetaOapg.properties.framework
    load_model_fn_module_path: MetaOapg.properties.load_model_fn_module_path
    location: MetaOapg.properties.location
    load_predict_fn_module_path: MetaOapg.properties.load_predict_fn_module_path

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flavor"]) -> MetaOapg.properties.flavor:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["framework"]
    ) -> MetaOapg.properties.framework:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["load_model_fn_module_path"]
    ) -> MetaOapg.properties.load_model_fn_module_path:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["load_predict_fn_module_path"]
    ) -> MetaOapg.properties.load_predict_fn_module_path:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["location"]
    ) -> MetaOapg.properties.location:
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "flavor",
                "framework",
                "load_model_fn_module_path",
                "load_predict_fn_module_path",
                "location",
                "requirements",
                "app_config",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["flavor"]
    ) -> MetaOapg.properties.flavor:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["framework"]
    ) -> MetaOapg.properties.framework:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["load_model_fn_module_path"]
    ) -> MetaOapg.properties.load_model_fn_module_path:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["load_predict_fn_module_path"]
    ) -> MetaOapg.properties.load_predict_fn_module_path:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["location"]
    ) -> MetaOapg.properties.location:
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "flavor",
                "framework",
                "load_model_fn_module_path",
                "load_predict_fn_module_path",
                "location",
                "requirements",
                "app_config",
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
            str,
        ],
        requirements: typing.Union[
            MetaOapg.properties.requirements,
            list,
            tuple,
        ],
        framework: typing.Union[
            MetaOapg.properties.framework,
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
        load_model_fn_module_path: typing.Union[
            MetaOapg.properties.load_model_fn_module_path,
            str,
        ],
        location: typing.Union[
            MetaOapg.properties.location,
            str,
        ],
        load_predict_fn_module_path: typing.Union[
            MetaOapg.properties.load_predict_fn_module_path,
            str,
        ],
        app_config: typing.Union[
            MetaOapg.properties.app_config, dict, frozendict.frozendict, schemas.Unset
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
    ) -> "ZipArtifactFlavor":
        return super().__new__(
            cls,
            *_args,
            flavor=flavor,
            requirements=requirements,
            framework=framework,
            load_model_fn_module_path=load_model_fn_module_path,
            location=location,
            load_predict_fn_module_path=load_predict_fn_module_path,
            app_config=app_config,
            _configuration=_configuration,
            **kwargs,
        )


from launch_client.model.custom_framework import CustomFramework
from launch_client.model.pytorch_framework import PytorchFramework
from launch_client.model.tensorflow_framework import TensorflowFramework
