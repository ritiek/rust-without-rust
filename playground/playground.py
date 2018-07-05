import json
import sys
import argparse

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def get_arguments(raw_args=None):
    parser = argparse.ArgumentParser(
            description="Use Python to execute simple Rust code"
                        "by running it on https://play.rust-lang.org/",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("file",
                        metavar="FILE",
                        help="path to file containing Rust code")

    parser.add_argument("--release",
                        default=False,
                        action="store_true",
                        help="build artifacts in release mode,"
                             "with optimizations")

    parser.add_argument("--channel",
                        default="stable",
                        choices={"stable", "beta", "nightly"},
                        help="set Rust channel")

    parser.add_argument("--target",
                        default="asm",
                        choices={"ast", "asm", "mir", "llvm-ir", "wasm"},
                        help="build for the target triple")

    parsed = parser.parse_args(raw_args)
    return parsed


def parse_json(code, channel="stable", mode="debug", target="ast"):

    json_data = { "channel"          : channel,
                  "code"             : content.decode("utf-8"),
                  "crateType"        : "bin",
                  "mode"             : mode,
                  "tests"            : False,
                  "assemblyFlavor"   : "att",
                  "demangleAssembly" : "demangle",
                  "target"           : target,
                  "tests"            : False,
                  "execute"          : target == "ast" }

    return json_data


def make_request(json_data):
    if json_data["execute"]:
        url = "http://play.rust-lang.org/execute"
    else:
        url = "http://play.rust-lang.org/compile"
    data = json.dumps(json_data).encode("utf-8")
    response = urlopen(url, data)
    return json.loads(response.read())


def filter_results(results):
    for key, value in results.items():
        results[key] = str(value).strip()
    return results


def command_line():
    args = get_arguments()

    with open(args.file, "rb") as raw_data:
        content = raw_data.read()

    if args.release:
        mode = "release"
    else:
        mode = "debug"

    json_data = parse_json(content,
                           channel=args.channel,
                           mode=mode,
                           target=args.target)

    response = make_request(json_data)

    results = filter_results(response)

    if "code" in results:
        print(results["code"])

    print(results["stderr"])
    print(results["stdout"])


if __name__ == "__main__":  # pragma: no cover
    command_line()
