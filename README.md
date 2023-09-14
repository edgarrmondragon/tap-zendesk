# `tap-zendesk`

Singer tap for Zendesk.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Supported Python Versions

* 3.8
* 3.9
* 3.10
* 3.11

## Supported streams

| Stream name | API endpoint                          |
| ----------- | ------------------------------------- |
| users       | [`GET /api/v2/users`][api-list-users] |

Other streams are available for sponsors.

The following streams will be made generally available when the corresponding sponsorship milestone is reached:

| Stream name     | API endpoint                                                           | Sponsorship Milestone |
| --------------- | ---------------------------------------------------------------------- | --------------------- |
| tickets         | [`GET /api/v2/tickets`][api-list-tickets]                              | $50                   |
| groups          | [`GET /api/v2/groups`][api-list-groups]                                | $100                  |
| ticket_comments | [`GET /api/v2/tickets/{ticket_id}/comments`][api-list-ticket-comments] | $500                  |

### Incremental Replication

Incremental replication is not supported. See https://github.com/edgarrmondragon/tap-zendesk/issues/3.

## Settings

| Setting              | Required | Default | Description                                                                                                                                 |
| :------------------- | :------: | :-----: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| subdomain            |   True   |  None   | Zendesk subdomain                                                                                                                           |
| auth                 |   True   |  None   | Zendesk authentication method                                                                                                               |
| auth.type            |   True   |  None   | See [supported authenticated methods](#source-authentication-and-authorization)                                                             |
| auth.api_token       |    -     |  None   | Zendesk API token for `api_token` authentication                                                                                            |
| auth.email_address   |    -     |  None   | Zendesk Email for `api_token` authentication                                                                                                |
| start_date           |  False   |  None   | Earliest datetime to get data from                                                                                                          |
| stream_maps          |  False   |  None   | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config    |  False   |  None   | User-defined config values to be used within map expressions.                                                                               |
| flattening_enabled   |  False   |  None   | 'True' to enable schema flattening and automatically expand nested properties.                                                              |
| flattening_max_depth |  False   |  None   | The max depth to flatten schemas.                                                                                                           |
| batch_config         |  False   |  None   |                                                                                                                                             |

A full list of supported settings and capabilities is available by running: `tap-zendesk --about`

### Source Authentication and Authorization

The following authentication methods are supported:

* [`api_token`](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token)

Planned:

* [`basic`](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#basic-authentication)
* [`oauth`](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#oauth-access-token)

## Usage

You can easily run `tap-zendesk` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-zendesk --version
tap-zendesk --help
tap-zendesk --config CONFIG --discover > ./catalog.json
```

### Selected custom fields

Nested custom fields required the user to declare them in `schema` object of the tap [catalog](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#the-catalog).

Using Meltano, this becomes simple using the [`schema`](https://docs.meltano.com/concepts/plugins#schema-extra) and [`metadata`](https://docs.meltano.com/concepts/plugins/#metadata-extra) extras:

```yaml
# meltano.yml
plugins:
  extractors:
  - name: tap-zendesk

    # Add custom fields to the schema
    schema:
      users:
        user_fields:
          type: object
          properties:
            test_custom_field:
              type: [string, "null"]
            test_pii_field:
              type: [integer, "null"]

    # Select the custom fields you want to sync
    select:
      - users.*
      - "users.user_fields"
      - "users.user_fields.*"
      - "!users.user_fields.test_pii_field"
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-zendesk` CLI interface directly using `poetry run`:

```bash
poetry run tap-zendesk --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-zendesk
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-zendesk --version
# OR run a test `elt` pipeline:
meltano elt tap-zendesk target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.

[api-list-users]: https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users
[api-list-tickets]: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#list-tickets
[api-list-groups]: https://developer.zendesk.com/api-reference/ticketing/groups/groups/#list-groups
[api-list-ticket-comments]: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/#list-comments
