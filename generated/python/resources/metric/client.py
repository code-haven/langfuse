# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import FintoLangfuseEnvironment
from .types.create_metric_request import CreateMetricRequest
from .types.metric import Metric


class MetricClient:
    def __init__(self, *, environment: FintoLangfuseEnvironment):
        self._environment = environment

    def create(self, *, request: CreateMetricRequest) -> Metric:
        _response = httpx.request(
            "POST", urllib.parse.urljoin(f"{self._environment}/", "api/metrics"), json=jsonable_encoder(request)
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Metric, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)