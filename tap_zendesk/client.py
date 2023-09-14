"""REST client handling, including ZendeskStream base class."""

from __future__ import annotations

import typing as t

from requests.auth import HTTPBasicAuth
from singer_sdk import RESTStream
from singer_sdk.helpers._typing import TypeConformanceLevel

if t.TYPE_CHECKING:
    from singer_sdk.authenticators import BasicAuthenticator


class ZendeskStream(RESTStream):
    """Zendesk stream class."""

    next_page_token_jsonpath = "$.next_page"  # noqa: S105
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    @property
    def url_base(self) -> str:
        """API root."""
        return f"https://{self.config['subdomain']}.zendesk.com"

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        auth = self.config["auth"]
        auth_type = auth["type"]

        if auth_type == "api_token":
            return HTTPBasicAuth(
                f"{auth['email_address']}/token",
                auth["api_token"],
            )
        message = f"Unsupported auth type: {auth_type}"
        raise ValueError(message)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ARG002, ANN401
    ) -> dict[str, t.Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        params: dict = {}
        return params
