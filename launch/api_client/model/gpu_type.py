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


class GpuType(schemas.EnumBase, schemas.StrSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Lists allowed GPU types for Launch.
    """

    class MetaOapg:
        enum_value_to_name = {
            "nvidia-tesla-t4": "TESLAT4",
            "nvidia-ampere-a10": "AMPEREA10",
            "nvidia-a100": "A100",
        }

    @schemas.classproperty
    def TESLAT4(cls):
        return cls("nvidia-tesla-t4")

    @schemas.classproperty
    def AMPEREA10(cls):
        return cls("nvidia-ampere-a10")

    @schemas.classproperty
    def A100(cls):
        return cls("nvidia-a100")
