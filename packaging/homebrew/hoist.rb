# A Homebrew formula for Hoist's release binaries, as a template: the
# release workflow fills in the version and the archives' checksums with
# packaging/homebrew/fill.sh and attaches the result to the release as
# hoist.rb. Homebrew installs it from a tap, a repository named
# homebrew-tap under the same account, as Formula/hoist.rb
# (docs/releasing.md).
class Hoist < Formula
  desc "Learn an LLM agent's next reads from its tool calls and serve them over MCP"
  homepage "https://hoist.alexnodeland.com/"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/alexnodeland/hoist/releases/download/v@VERSION@/hoist-aarch64-apple-darwin.tar.gz"
      sha256 "@SHA256_AARCH64_APPLE_DARWIN@"
    end
    on_intel do
      url "https://github.com/alexnodeland/hoist/releases/download/v@VERSION@/hoist-x86_64-apple-darwin.tar.gz"
      sha256 "@SHA256_X86_64_APPLE_DARWIN@"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/alexnodeland/hoist/releases/download/v@VERSION@/hoist-aarch64-unknown-linux-gnu.tar.gz"
      sha256 "@SHA256_AARCH64_UNKNOWN_LINUX_GNU@"
    end
    on_intel do
      url "https://github.com/alexnodeland/hoist/releases/download/v@VERSION@/hoist-x86_64-unknown-linux-gnu.tar.gz"
      sha256 "@SHA256_X86_64_UNKNOWN_LINUX_GNU@"
    end
  end

  def install
    bin.install "hoist", "hoist-mcp", "hoist-procedure", "hoist-mcp-demo", "hoist-console"
    generate_completions_from_executable(bin/"hoist", "completions")
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/hoist --version")
    assert_match version.to_s, shell_output("#{bin}/hoist-mcp --version")
  end
end
