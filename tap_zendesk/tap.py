"""Zendesk tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_zendesk import streams


class TapZendesk(Tap):
    """Singer tap for Zendesk."""

    name = "tap-zendesk"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "subdomain",
            th.StringType,
            description="Zendesk subdomain",
            required=True,
        ),
        th.Property(
            "auth",
            th.DiscriminatedUnion(
                "type",
                api_token=th.ObjectType(
                    th.Property("email_address", th.StringType, required=True),
                    th.Property("api_token", th.StringType, required=True),
                ),
            ),
            description="Zendesk authentication method",
            required=True,
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Zendesk streams.
        """
        return [
            streams.Users(tap=self),
        ]
