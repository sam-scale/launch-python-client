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

class CompletionSyncV1Request(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request object for a synchronous prompt completion task.
    """

    class MetaOapg:
        required = {
            "max_new_tokens",
            "temperature",
            "prompt",
        }

        class properties:
            max_new_tokens = schemas.IntSchema
            prompt = schemas.StrSchema

            class temperature(schemas.NumberSchema):
                pass

            class frequency_penalty(schemas.NumberSchema):
                pass

            class guided_choice(schemas.ListSchema):
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
                ) -> "guided_choice":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            guided_grammar = schemas.StrSchema
            guided_json = schemas.DictSchema
            guided_regex = schemas.StrSchema
            include_stop_str_in_output = schemas.BoolSchema

            class presence_penalty(schemas.NumberSchema):
                pass
            return_token_log_probs = schemas.BoolSchema

            class stop_sequences(schemas.ListSchema):
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
                ) -> "stop_sequences":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            class top_k(schemas.IntSchema):
                pass

            class top_p(schemas.NumberSchema):
                pass
            __annotations__ = {
                "max_new_tokens": max_new_tokens,
                "prompt": prompt,
                "temperature": temperature,
                "frequency_penalty": frequency_penalty,
                "guided_choice": guided_choice,
                "guided_grammar": guided_grammar,
                "guided_json": guided_json,
                "guided_regex": guided_regex,
                "include_stop_str_in_output": include_stop_str_in_output,
                "presence_penalty": presence_penalty,
                "return_token_log_probs": return_token_log_probs,
                "stop_sequences": stop_sequences,
                "top_k": top_k,
                "top_p": top_p,
            }
    max_new_tokens: MetaOapg.properties.max_new_tokens
    temperature: MetaOapg.properties.temperature
    prompt: MetaOapg.properties.prompt

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_new_tokens"]) -> MetaOapg.properties.max_new_tokens: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt"]) -> MetaOapg.properties.prompt: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["frequency_penalty"]
    ) -> MetaOapg.properties.frequency_penalty: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guided_choice"]) -> MetaOapg.properties.guided_choice: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guided_grammar"]) -> MetaOapg.properties.guided_grammar: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guided_json"]) -> MetaOapg.properties.guided_json: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guided_regex"]) -> MetaOapg.properties.guided_regex: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["include_stop_str_in_output"]
    ) -> MetaOapg.properties.include_stop_str_in_output: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["presence_penalty"]
    ) -> MetaOapg.properties.presence_penalty: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["return_token_log_probs"]
    ) -> MetaOapg.properties.return_token_log_probs: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_sequences"]) -> MetaOapg.properties.stop_sequences: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_k"]) -> MetaOapg.properties.top_k: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_p"]) -> MetaOapg.properties.top_p: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "max_new_tokens",
                "prompt",
                "temperature",
                "frequency_penalty",
                "guided_choice",
                "guided_grammar",
                "guided_json",
                "guided_regex",
                "include_stop_str_in_output",
                "presence_penalty",
                "return_token_log_probs",
                "stop_sequences",
                "top_k",
                "top_p",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["max_new_tokens"]
    ) -> MetaOapg.properties.max_new_tokens: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt"]) -> MetaOapg.properties.prompt: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["frequency_penalty"]
    ) -> typing.Union[MetaOapg.properties.frequency_penalty, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["guided_choice"]
    ) -> typing.Union[MetaOapg.properties.guided_choice, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["guided_grammar"]
    ) -> typing.Union[MetaOapg.properties.guided_grammar, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["guided_json"]
    ) -> typing.Union[MetaOapg.properties.guided_json, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["guided_regex"]
    ) -> typing.Union[MetaOapg.properties.guided_regex, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["include_stop_str_in_output"]
    ) -> typing.Union[MetaOapg.properties.include_stop_str_in_output, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["presence_penalty"]
    ) -> typing.Union[MetaOapg.properties.presence_penalty, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["return_token_log_probs"]
    ) -> typing.Union[MetaOapg.properties.return_token_log_probs, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["stop_sequences"]
    ) -> typing.Union[MetaOapg.properties.stop_sequences, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["top_k"]
    ) -> typing.Union[MetaOapg.properties.top_k, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["top_p"]
    ) -> typing.Union[MetaOapg.properties.top_p, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "max_new_tokens",
                "prompt",
                "temperature",
                "frequency_penalty",
                "guided_choice",
                "guided_grammar",
                "guided_json",
                "guided_regex",
                "include_stop_str_in_output",
                "presence_penalty",
                "return_token_log_probs",
                "stop_sequences",
                "top_k",
                "top_p",
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
        max_new_tokens: typing.Union[
            MetaOapg.properties.max_new_tokens,
            decimal.Decimal,
            int,
        ],
        temperature: typing.Union[
            MetaOapg.properties.temperature,
            decimal.Decimal,
            int,
            float,
        ],
        prompt: typing.Union[
            MetaOapg.properties.prompt,
            str,
        ],
        frequency_penalty: typing.Union[
            MetaOapg.properties.frequency_penalty, decimal.Decimal, int, float, schemas.Unset
        ] = schemas.unset,
        guided_choice: typing.Union[MetaOapg.properties.guided_choice, list, tuple, schemas.Unset] = schemas.unset,
        guided_grammar: typing.Union[MetaOapg.properties.guided_grammar, str, schemas.Unset] = schemas.unset,
        guided_json: typing.Union[
            MetaOapg.properties.guided_json, dict, frozendict.frozendict, schemas.Unset
        ] = schemas.unset,
        guided_regex: typing.Union[MetaOapg.properties.guided_regex, str, schemas.Unset] = schemas.unset,
        include_stop_str_in_output: typing.Union[
            MetaOapg.properties.include_stop_str_in_output, bool, schemas.Unset
        ] = schemas.unset,
        presence_penalty: typing.Union[
            MetaOapg.properties.presence_penalty, decimal.Decimal, int, float, schemas.Unset
        ] = schemas.unset,
        return_token_log_probs: typing.Union[
            MetaOapg.properties.return_token_log_probs, bool, schemas.Unset
        ] = schemas.unset,
        stop_sequences: typing.Union[MetaOapg.properties.stop_sequences, list, tuple, schemas.Unset] = schemas.unset,
        top_k: typing.Union[MetaOapg.properties.top_k, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        top_p: typing.Union[MetaOapg.properties.top_p, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
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
    ) -> "CompletionSyncV1Request":
        return super().__new__(
            cls,
            *_args,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            prompt=prompt,
            frequency_penalty=frequency_penalty,
            guided_choice=guided_choice,
            guided_grammar=guided_grammar,
            guided_json=guided_json,
            guided_regex=guided_regex,
            include_stop_str_in_output=include_stop_str_in_output,
            presence_penalty=presence_penalty,
            return_token_log_probs=return_token_log_probs,
            stop_sequences=stop_sequences,
            top_k=top_k,
            top_p=top_p,
            _configuration=_configuration,
            **kwargs,
        )
