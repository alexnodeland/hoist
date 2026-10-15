---
description: The environment variables Hoist reads - the optional TypeSafe key and its settings, the redaction salt, the variables for upstream headers, and the console's settings.
---

# Environment variables

Hoist needs no environment variable to record sessions, learn flows with the habit alone, serve them with the `reach` or `habit` decider, review, audit, promote, redact, or run a procedure. The TypeSafe variables matter only for what asks a System-One model ([when a key is needed](#when-a-key-is-needed)).

The wrapped server inherits the proxy's environment, so the variables a server needs go in the host's `env` block as usual. The proxy never records its environment.

## The System-One model

These are read by every command that asks TypeSafe's System-One model, Jev.

### `TYPESAFE_API_KEY`

The key for Jev. Optional: only the arbiter decider, the confirmation judge and some offline commands need it. Never logged.

### `TYPESAFE_API_KEY_FILE`

A file holding the key, read when `TYPESAFE_API_KEY` is not set. Useful when the proxy runs under an agent's process, which should not hold the key itself: the process gets the file's path, not the key.

### `TYPESAFE_BASE_URL`

Where Jev is. Default `https://api.typesafe.ai`.

### `TYPESAFE_DEFAULT_MODEL`

The model id to request when `--oracle-model` is not given. Default `jev-latest`.

### `SSL_CERT_FILE`

A PEM bundle of extra root certificates for the connection to Jev, such as a network proxy's.

## Everything else

### `HOIST_REDACT_SALT`

The salt `hoist redact` hashes values with. `--salt-env` names another variable. Keep it secret, and keep it the same for batches whose hashes should match.

### Upstream header values

`hoist-mcp --upstream-header NAME=VAR` sends the header `NAME` to a Streamable HTTP server with the value of the variable `VAR`, such as `ORDERS_AUTH` holding `Bearer …`. Any variable name works. The values are never logged.

### `HOME`

Where a leading `~` points in the proxy's path options, in `hoist init --flow` and in the console's job paths, and where `hoist doctor` and the console look for `~/.hoist` (the console's unless `HOIST_HOME` is set). `USERPROFILE` stands in when `HOME` is not set.

## The console

`hoist-console` reads these when the option in parentheses is not given ([the console](/guide/console)). Its jobs run the `hoist` CLI with the console's own environment, so a job that fits an arbiter needs `TYPESAFE_API_KEY` where the console runs, and `redact` needs `HOIST_REDACT_SALT`.

### `HOIST_HOME`

The data directory the console serves (`--data`). Default `~/.hoist`.

### `HOIST_CONSOLE_LISTEN`

The address it listens on (`--listen`). Default `127.0.0.1:7878`; the container image sets `0.0.0.0:8080`, and is published on 127.0.0.1 only.

### `HOIST_CONSOLE_TOKEN`

The token the API requires (`--token`). A token given this way is never printed, and keeps the console's URL the same across restarts. Default: a new token at each start, printed in the URL to open.

### `BROWSER`

The program `--open` opens the console's URL with. Default: the system's (`xdg-open`; `open` on macOS; `start` on Windows).

### `HOIST_UID`, `HOIST_GID`

For [`compose.yaml`](https://github.com/alexnodeland/hoist/blob/main/compose.yaml) only: the user and group the console's container runs as, so that the files it writes in your `~/.hoist` are yours.

## For development

### `HOIST_BLESS`

For the test suite. Set while running `cargo test`, it rewrites the generated documentation, the [CLI reference](./cli) and the examples in [reviewing flows](./review), instead of failing on a difference.

## When a key is needed

A command asks Jev, and needs `TYPESAFE_API_KEY` (or `TYPESAFE_API_KEY_FILE`), only when its answers are not already in the replay cache and:

- `hoist-mcp` serves a flow with its arbiter (`--flow-decider arbiter`, the default, with a flow that has one) or runs the confirmation judge (`--confirm-judge`), with `--oracle jev` (the default);
- `hoist learn` fits an arbiter, which it does unless given `--habit-only` or `--arbiter-from`;
- `hoist serve` or `flow-serve` decides with the arbiter, with `--oracle jev` (the default of `serve`);
- `hoist phase0`, `confirm`, `ask`, `audit` or `promote` runs with `--oracle jev`, or `hoist match` runs (its default oracle is `jev`);
- `hoist jev-check`, which checks the key.

Everything else asks nothing. With `--oracle replay`, commands read the cache only; with `--oracle mock`, they check the pipeline for free.

::: tip Serving with no key
`hoist learn --habit-only` and `hoist-mcp --flow-decider reach` (or `habit`) send nothing to any model and need no key.
:::

## Related

- [Deciders](/guide/concepts/deciders): what the arbiter does with the key
- [Privacy: what leaves the machine](./privacy#what-leaves-the-machine)
