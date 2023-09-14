"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_zendesk.tap import TapZendesk

load_dotenv()

SAMPLE_CONFIG: dict[str, Any] = {
    "subdomain": os.environ.get("TAP_ZENDESK_SUBDOMAIN"),
    "auth": {
        "type": "api_token",
        "email_address": os.environ.get("TAP_ZENDESK_AUTH_EMAIL_ADDRESS"),
        "api_token": os.environ.get("TAP_ZENDESK_AUTH_API_TOKEN"),
    },
}

StandardTapTests = get_tap_test_class(
    TapZendesk,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        max_records_limit=10,
    ),
)


class TestTapZendesk(StandardTapTests):
    """Run standard tap tests on Zendesk."""
