# Installing Hoist

Hoist is five binaries, installed together:

- `hoist`, the CLI: `learn`, `flow-show`, `flow-diff`, `audit`, `promote`, `redact`, `init`, `doctor` and the rest ([the CLI reference](cli.md));
- `hoist-mcp`, the MCP proxy that an MCP host runs in place of a server's command;
- `hoist-procedure`, which runs a compiled procedure against an MCP server;
- `hoist-mcp-demo`, a tiny MCP server for trying the proxy, which [the quickstart](../examples/quickstart/README.md) uses;
- `hoist-console`, the web console over `~/.hoist`: servers, sessions, flows and jobs ([the console](console.md)). Releases carry it from the first after 0.1.0.

| Way | Where | Needs |
|---|---|---|
| [Release binaries](#release-binaries) with `install.sh` | Linux x86_64 and aarch64 with glibc 2.35 or later, macOS (Apple silicon and Intel) | curl or wget |
| [`install.ps1`](#windows) | Windows x64 | PowerShell |
| [Homebrew](#homebrew) | macOS, Linux | the tap, which does not exist yet |
| [Docker](#docker) | anywhere Docker runs, linux/amd64 and linux/arm64 | Docker |
| [From source](#from-source) | anywhere Rust 1.88 or later runs | Rust |

Release archives, `install.sh`, `install.ps1` and the container image come with every release, from 0.1.0 on; until 0.1.0 is tagged, [install from source](#from-source). Then [check the installation](#check-it-hoist-doctor) and [add shell completions](#shell-completions).

## Release binaries

```sh
curl -fsSL https://github.com/alexnodeland/hoist/releases/latest/download/install.sh | sh
```

[`install.sh`](../install.sh) picks the archive for the system, downloads it and the release's `SHA256SUMS`, checks the archive's checksum, and copies the binaries into `~/.local/bin`. It changes nothing else: if that directory is not on PATH, it prints the line to add. To read it before running it, download it, then `sh install.sh`. Its options:

- `--version v0.2.0` installs that release instead of the latest. A pre-release (`v0.2.0-rc.1`) is installed only when named.
- `--prefix DIR` installs into `DIR/bin`: `curl -fsSL https://github.com/alexnodeland/hoist/releases/latest/download/install.sh | sudo sh -s -- --prefix /usr/local`.
- `--base-url URL` fetches the release's files from a mirror instead of GitHub.

By hand, download the archive for your system and `SHA256SUMS` from [the release](https://github.com/alexnodeland/hoist/releases), check it, and copy the binaries onto PATH:

```sh
sha256sum --ignore-missing --check SHA256SUMS    # macOS: grep hoist-aarch64-apple-darwin.tar.gz SHA256SUMS | shasum -a 256 --check
tar -xzf hoist-x86_64-unknown-linux-gnu.tar.gz
cp hoist-x86_64-unknown-linux-gnu/hoist* ~/.local/bin/
```

| System | Archive |
|---|---|
| Linux x86_64 | `hoist-x86_64-unknown-linux-gnu.tar.gz` |
| Linux aarch64 | `hoist-aarch64-unknown-linux-gnu.tar.gz` |
| macOS, Apple silicon | `hoist-aarch64-apple-darwin.tar.gz` |
| macOS, Intel | `hoist-x86_64-apple-darwin.tar.gz` |
| Windows x64 | `hoist-x86_64-pc-windows-msvc.zip` |

Each archive holds the binaries, `LICENSE` and `README.md`.

- **Linux** binaries are built on Ubuntu 22.04, so they need glibc 2.35 or later: Debian 12, Ubuntu 22.04, Fedora 36 and later. On Alpine and other musl systems, use the [container image](#docker) or [build from source](#from-source).
- **macOS** binaries are not signed with a Developer ID or notarized. A file downloaded with curl, as `install.sh` does, runs as it is. An archive downloaded with a browser is quarantined, and macOS refuses to run its binaries until the attribute is removed: `xattr -d com.apple.quarantine ~/.local/bin/hoist*`.

## Windows

In PowerShell:

```powershell
irm https://github.com/alexnodeland/hoist/releases/latest/download/install.ps1 | iex
```

[`install.ps1`](../install.ps1) does what `install.sh` does, into `%LOCALAPPDATA%\Programs\hoist\bin`, and prints the command that adds it to your PATH. With options: `& ([scriptblock]::Create((irm https://github.com/alexnodeland/hoist/releases/latest/download/install.ps1))) -Version v0.2.0 -Prefix C:\tools\hoist`.

The Windows build is compiled and run with `--version` for each release; CI runs the tests on Linux, and the console's on macOS and Windows as well. The quickstart needs a POSIX shell: run it in WSL or in the container.

## Homebrew

Once the tap exists ([releasing](releasing.md#homebrew)):

```sh
brew install alexnodeland/tap/hoist
```

The formula installs the release binaries and the completions for bash, zsh and fish.

## Docker

```sh
docker run --rm ghcr.io/alexnodeland/hoist --version
docker run --rm --entrypoint /usr/local/share/hoist/quickstart/run.sh ghcr.io/alexnodeland/hoist
```

`ghcr.io/alexnodeland/hoist` is built from the [Dockerfile](../Dockerfile) for linux/amd64 and linux/arm64, tagged with each release's version (`0.2.0`), its minor version (`0.2`) and `latest`. It is Debian 13 slim with the binaries in `/usr/local/bin` and the quickstart in `/usr/local/share/hoist/quickstart`. It runs `hoist` as the user 10001, with `HOME` and the working directory `/data`, so `~/.hoist` is `/data/.hoist`.

To keep the logs and flows, mount a directory there, and run as your own user so that the files are yours:

```sh
docker run --rm --user "$(id -u):$(id -g)" -v "$HOME/.hoist:/data/.hoist" \
  ghcr.io/alexnodeland/hoist learn --sessions /data/.hoist/logs/notes \
  --domain notes --habit-only --out /data/.hoist/notes.flow.json
```

`--entrypoint hoist-mcp` (or `hoist-procedure`, `hoist-mcp-demo`) runs the other binaries. The image has no Node or Python, so as a host's MCP server it can only wrap a server it reaches over Streamable HTTP (`--upstream`), with `docker run -i`:

```json
{
  "mcpServers": {
    "orders": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--user", "1000:1000", "-v", "/home/me/.hoist:/data/.hoist",
               "--entrypoint", "hoist-mcp", "ghcr.io/alexnodeland/hoist",
               "--record", "/data/.hoist/logs/orders", "--domain", "orders",
               "--upstream", "https://example.com/mcp"]
    }
  }
}
```

**The console** has an image of its own, `ghcr.io/alexnodeland/hoist-console`, from the same build: `hoist-console` as the entrypoint, on port 8080, with a health check. [`compose.yaml`](../compose.yaml) runs it over your `~/.hoist` (`HOIST_UID=$(id -u) HOIST_GID=$(id -g) docker compose up -d`); [the console's page](console.md#in-a-container) has the rest.

To build the images from a checkout: `docker build -t hoist .`, and `docker build --target console -t hoist-console .` for the console. Behind a TLS-inspecting proxy, pass the proxy's CA bundle as a build secret and the proxy as a build argument: `docker build --secret id=ca,src=ca.pem --build-arg HTTPS_PROXY=http://proxy:3128 -t hoist .`. Cargo uses them while it builds; neither reaches the image.

## From source

With Rust 1.88 or later ([rustup](https://rustup.rs)):

```sh
cargo install --locked --git https://github.com/alexnodeland/hoist hoist-report hoist-mcp
```

That builds `main`; add `--tag vX.Y.Z` to build a release.

`hoist-report` installs `hoist`, and `hoist-mcp` installs `hoist-mcp`, `hoist-procedure` and `hoist-mcp-demo`. From a checkout:

```sh
cargo install --locked --path crates/hoist-report
cargo install --locked --path crates/hoist-mcp
```

`hoist-console` embeds its UI, so build the UI first (Node 22.12 or later), then install it:

```sh
npm --prefix console ci && npm --prefix console run build
cargo install --locked --path crates/hoist-console
```

No release of Hoist is on crates.io yet, only empty 0.0.0 placeholders that hold the crates' names ([why](releasing.md#cratesio)). `cargo install hoist` installs an unrelated tool; use `--git` as above.

## Check it: `hoist doctor`

```sh
hoist doctor
```

In the container image, with nothing recorded yet, it prints:

```text
hoist 0.1.0 (/usr/local/bin/hoist)

ok       hoist-mcp 0.1.0 (/usr/local/bin/hoist-mcp)
ok       hoist-procedure 0.1.0 (/usr/local/bin/hoist-procedure)
ok       hoist-mcp-demo 0.1.0 (/usr/local/bin/hoist-mcp-demo)
note     /data/.hoist does not exist yet; `hoist-mcp --record` creates it
note     TYPESAFE_API_KEY is not set. It is optional: recording, `learn --habit-only`, `flow-show`, `flow-diff`, `audit`, `promote` and serving with `--flow-decider habit` or `reach` need no key. With one, hoist asks TypeSafe's Jev: `learn` fits an arbiter, the proxy serves with `--flow-decider arbiter` and runs the confirmation judge, and `phase0 --oracle jev` measures Jev on τ²-bench.
note     no flows in ~/.hoist yet (`hoist learn` writes one)
note     no recorded sessions in ~/.hoist yet
```

It finds the other three binaries on PATH and checks that they are the same version as `hoist`, checks that `~/.hoist` is writable, says whether `TYPESAFE_API_KEY` (or `TYPESAFE_API_KEY_FILE`) is set, without showing it, and lists the flows and recorded sessions in `~/.hoist`. It exits with 1 when something needs fixing, such as `hoist-mcp` missing from PATH. It makes no network request; `hoist doctor --network` also asks Jev one question when a key is set, as `hoist jev-check` does.

## Shell completions

`hoist completions SHELL` prints the completion script for bash, zsh, fish, powershell or elvish:

```sh
# bash (with bash-completion 2)
mkdir -p ~/.local/share/bash-completion/completions
hoist completions bash > ~/.local/share/bash-completion/completions/hoist

# zsh: into a directory on fpath, set in ~/.zshrc before compinit
mkdir -p ~/.zfunc
hoist completions zsh > ~/.zfunc/_hoist
#   in ~/.zshrc: fpath=(~/.zfunc $fpath); autoload -Uz compinit; compinit

# fish
mkdir -p ~/.config/fish/completions
hoist completions fish > ~/.config/fish/completions/hoist.fish
```

```powershell
# PowerShell: add this line to $PROFILE
hoist completions powershell | Out-String | Invoke-Expression
```

For elvish, add `eval (hoist completions elvish | slurp)` to `~/.config/elvish/rc.elv`. Homebrew installs the bash, zsh and fish completions itself.

## Next

`hoist init` prints the configuration that runs your MCP server behind `hoist-mcp`, recording its sessions, for Claude Code, Claude Desktop, Cursor or VS Code, and the steps from there to a served flow:

```sh
hoist init --host claude-code --domain notes -- npx -y @modelcontextprotocol/server-filesystem ~/notes
```

[The quickstart](../examples/quickstart/README.md) runs the whole loop in about a second with no key, and [the walkthrough](walkthrough.md) runs it on the official MCP filesystem server.

## Uninstall

Delete the four binaries: `rm ~/.local/bin/hoist ~/.local/bin/hoist-mcp ~/.local/bin/hoist-procedure ~/.local/bin/hoist-mcp-demo` (or `brew uninstall hoist`, or `cargo uninstall hoist-report hoist-mcp`). `~/.hoist` holds the recorded sessions, the answer cache and the flows; delete it too if you want them gone.
