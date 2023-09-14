"""Stream type classes for tap-zendesk."""

from __future__ import annotations

from typing import ClassVar

from singer_sdk import typing as th

from tap_zendesk.client import ZendeskStream

ATTACHMENT_OBJECT = th.ObjectType(
    th.Property(
        "content_type",
        th.StringType,
        description='The content type of the image. Example value: "image/png"',
    ),
    th.Property(
        "content_url",
        th.StringType,
        description=(
            "A full URL where the attachment image file can be downloaded. The "
            "file may be hosted externally so take care not to inadvertently send "
            "Zendesk authentication credentials"
        ),
    ),
    th.Property(
        "deleted",
        th.BooleanType,
        description="If true, the attachment has been deleted",
    ),
    th.Property(
        "file_name",
        th.StringType,
        description="The name of the image file",
    ),
    th.Property(
        "height",
        th.IntegerType,
        description=(
            "The height of the image file in pixels. If height is unknown, returns "
            "null"
        ),
    ),
    th.Property(
        "id",
        th.IntegerType,
        description="Automatically assigned when created",
    ),
    th.Property(
        "inline",
        th.BooleanType,
        description=(
            "If true, the attachment is excluded from the attachment list and the "
            "attachment's URL can be referenced within the comment of a ticket. "
            "Default is false"
        ),
    ),
    th.Property(
        "malware_access_override",
        th.BooleanType,
        description=(
            "If true, you can download an attachment flagged as malware. If false, "
            "you can't download such an attachment."
        ),
    ),
    th.Property(
        "malware_scan_result",
        th.StringType,
        description=(
            "The result of the malware scan. There is a delay between the time the "
            "attachment is uploaded and when the malware scan is completed. "
            "Usually the scan is done within a few seconds, but high load "
            "conditions can delay the scan results. Possible values: "
            '"malware_found", "malware_not_found", "failed_to_scan", "not_scanned"'
        ),
    ),
    th.Property(
        "mapped_content_url",
        th.StringType,
        description="The URL the attachment image file has been mapped to",
    ),
    th.Property(
        "size",
        th.IntegerType,
        description="The size of the image file in bytes",
    ),
    th.Property(
        "thumbnails",
        # TODO(edgarrmondragon): Make this recursive  # noqa: TD003
        th.ArrayType(th.ObjectType()),
        description=(
            "An array of attachment objects. Note that photo thumbnails do not "
            "have thumbnails"
        ),
    ),
    th.Property(
        "url",
        th.StringType,
        description="A URL to access the attachment details",
    ),
    th.Property(
        "width",
        th.IntegerType,
        description=(
            "The width of the image file in pixels. If width is unknown, returns "
            "null"
        ),
    ),
)


class Users(ZendeskStream):
    """Users stream."""

    name = "users"
    path = "/api/v2/users.json"
    primary_keys: ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.users[*]"
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "active",
            th.BooleanType,
            description="false if the user has been deleted",
        ),
        th.Property(
            "alias",
            th.StringType,
            description="An alias displayed to end users",
        ),
        th.Property(
            "chat_only",
            th.BooleanType,
            description="Whether or not the user is a chat-only agent",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="The time the user was created",
        ),
        th.Property(
            "custom_role_id",
            th.IntegerType,
            description=(
                "A custom role if the user is an agent on the Enterprise plan or above"
            ),
        ),
        th.Property(
            "default_group_id",
            th.IntegerType,
            description="The id of the user's default group",
        ),
        th.Property(
            "details",
            th.StringType,
            description=(
                "Any details you want to store about the user, such as an address"
            ),
        ),
        th.Property(
            "email",
            th.EmailType,
            description=(
                "The primary email address of this user. If the primary email address "
                "is not verified, the secondary email address is used"
            ),
        ),
        th.Property(
            "external_id",
            th.StringType,
            description=(
                "A unique identifier from another system. The API treats the id as "
                'case insensitive. Example: "ian1" and "IAN1" are the same value.'
            ),
        ),
        th.Property(
            "iana_time_zone",
            th.StringType,
            description="The time-zone of this user",
        ),
        th.Property(
            "id",
            th.IntegerType,
            description="Automatically assigned when creating users",
        ),
        th.Property(
            "last_login_at",
            th.StringType,
            description=(
                "Last time the user signed in to Zendesk Support or made an API "
                "request using an API token or basic authentication"
            ),
        ),
        th.Property(
            "locale",
            th.StringType,
            description="The locale for this user",
        ),
        th.Property(
            "locale_id",
            th.IntegerType,
            description="The language identifier for this user",
        ),
        th.Property(
            "moderator",
            th.BooleanType,
            description="Designates whether the user has forum moderation capabilities",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The name of the user",
        ),
        th.Property(
            "notes",
            th.StringType,
            description="Any notes you want to store about the user",
        ),
        th.Property(
            "only_private_comments",
            th.BooleanType,
            description="true if the user can only create private comments",
        ),
        th.Property(
            "organization_id",
            th.IntegerType,
            description=(
                "The id of the user's organization. If the user has more than one "
                "organization memberships, the id of the user's default organization"
            ),
        ),
        th.Property(
            "phone",
            th.StringType,
            description="The primary phone number of this user",
        ),
        th.Property(
            "photo",
            ATTACHMENT_OBJECT,
            description=(
                "The user's profile picture represented as an Attachment object"
            ),
        ),
        th.Property(
            "remote_photo_url",
            th.StringType,
            description="A URL pointing to the user's profile picture.",
        ),
        th.Property(
            "report_csv",
            th.BooleanType,
            description=(
                "This parameter is inert and has no effect. It may be deprecated in "
                "the future. Previously, this parameter determined whether a user "
                "could access a CSV report in a legacy Guide dashboard. This dashboard "
                "has been removed."
            ),
        ),
        th.Property(
            "restricted_agent",
            th.BooleanType,
            description=(
                "If the agent has any restrictions; false for admins and unrestricted "
                "agents, true for other agents"
            ),
        ),
        th.Property(
            "role",
            th.StringType,
            description=(
                'The role of the user. Possible values: "end-user", "agent", "admin"'
            ),
        ),
        th.Property(
            "role_type",
            th.IntegerType,
            description=(
                "The user's role id. 0 for a custom agent, 1 for a light agent, 2 for "
                "a chat agent, 3 for a chat agent added to the Support account as a "
                "contributor (Chat Phase 4), 4 for an admin, and 5 for a billing admin"
            ),
        ),
        th.Property(
            "shared",
            th.BooleanType,
            description=(
                "If the user is shared from a different Zendesk Support instance. "
                "Ticket sharing accounts only"
            ),
        ),
        th.Property(
            "shared_agent",
            th.BooleanType,
            description=(
                "If the user is a shared agent from a different Zendesk Support "
                "instance. Ticket sharing accounts only"
            ),
        ),
        th.Property(
            "shared_phone_number",
            th.BooleanType,
            description="Whether the phone number is shared or not",
        ),
        th.Property(
            "signature",
            th.StringType,
            description=(
                "The user's signature. Only agents and admins can have signatures"
            ),
        ),
        th.Property(
            "suspended",
            th.BooleanType,
            description=(
                "If the agent is suspended. Tickets from suspended users are also "
                "suspended, and these users cannot sign in to the end user portal"
            ),
        ),
        th.Property(
            "tags",
            th.ArrayType(th.StringType),
            description=(
                "The user's tags. Only present if your account has user tagging enabled"
            ),
        ),
        th.Property(
            "ticket_restriction",
            th.StringType,
            description=(
                "Specifies which tickets the user has access to. Possible values are: "
                '"organization", "groups", "assigned", "requested", null'
            ),
        ),
        th.Property(
            "time_zone",
            th.StringType,
            description="The time-zone of this user",
        ),
        th.Property(
            "two_factor_auth_enabled",
            th.BooleanType,
            description="If two factor authentication is enabled",
        ),
        th.Property(
            "updated_at",
            th.DateTimeType,
            description="The time of the last update of the user",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The API url of this user",
        ),
        th.Property(
            "user_fields",
            th.ObjectType(additional_properties=True),
        ),
        th.Property(
            "verified",
            th.BooleanType,
            description="Any of the user's identities is verified",
        ),
    ).to_dict()
