# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3
from launch.api_client import schemas  # noqa: F401
from launch.api_client import api_client, exceptions
from launch.api_client.model.create_llm_model_endpoint_v1_request import CreateLLMModelEndpointV1Request
from launch.api_client.model.create_llm_model_endpoint_v1_response import (
    CreateLLMModelEndpointV1Response,
)
from launch.api_client.model.http_validation_error import HTTPValidationError
from urllib3._collections import HTTPHeaderDict

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateLLMModelEndpointV1Request


request_body_create_llm_model_endpoint_v1_request = api_client.RequestBody(
    content={
        "application/json": api_client.MediaType(schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    "HTTPBasic",
]
SchemaFor200ResponseBodyApplicationJson = CreateLLMModelEndpointV1Response


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[SchemaFor200ResponseBodyApplicationJson,]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/json": api_client.MediaType(schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[SchemaFor422ResponseBodyApplicationJson,]
    headers: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        "application/json": api_client.MediaType(schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    "200": _response_for_200,
    "422": _response_for_422,
}
_all_accept_content_types = ("application/json",)


class BaseApi(api_client.Api):
    @typing.overload
    def _create_model_endpoint_v1_llm_model_endpoints_post_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def _create_model_endpoint_v1_llm_model_endpoints_post_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def _create_model_endpoint_v1_llm_model_endpoints_post_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _create_model_endpoint_v1_llm_model_endpoints_post_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def _create_model_endpoint_v1_llm_model_endpoints_post_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Create Model Endpoint
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                "The required body parameter has an invalid value of: unset. Set a valid value instead"
            )
        _fields = None
        _body = None
        serialized_data = request_body_create_llm_model_endpoint_v1_request.serialize(body, content_type)
        _headers.add("Content-Type", content_type)
        if "fields" in serialized_data:
            _fields = serialized_data["fields"]
        elif "body" in serialized_data:
            _body = serialized_data["body"]
        response = self.api_client.call_api(
            resource_path=used_path,
            method="post".upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(status=response.status, reason=response.reason, api_response=api_response)

        return api_response


class CreateModelEndpointV1LlmModelEndpointsPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def create_model_endpoint_v1_llm_model_endpoints_post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def create_model_endpoint_v1_llm_model_endpoints_post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def create_model_endpoint_v1_llm_model_endpoints_post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def create_model_endpoint_v1_llm_model_endpoints_post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def create_model_endpoint_v1_llm_model_endpoints_post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_model_endpoint_v1_llm_model_endpoints_post_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = "application/json",
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_model_endpoint_v1_llm_model_endpoints_post_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
