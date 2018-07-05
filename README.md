# rust-without-rust

[![Pypi Version](https://img.shields.io/pypi/v/rust-playground.svg)](https://pypi.org/project/rust-without-rust)
[![Build Status](https://travis-ci.org/ritiek/rust-without-rust.svg?branch=master)](https://travis-ci.org/ritiek/rust-without-rust)

This is a small tool written in Python which allows you to compile simple
Rust code through http://play.rust-lang.org.

## Installation

You can install this package from PyPi.
```
pip install rust-playground
```

You can also clone this repository locally and run setup.py.
```
python setup.py install
```

## Usage

```
usage: playground [-h] [--release] [--channel {stable,nightly,beta}]
                  [--target {llvm-ir,wasm,asm,mir,ast}] [--disable-color]
                  FILE

Use Python to execute simple Rust code by running it on https://play.rust-
lang.org/

positional arguments:
  FILE                  path to file containing Rust code

optional arguments:
  -h, --help            show this help message and exit
  --release             build artifacts in release mode, with optimizations
                        (default: False)
  --channel {stable,nightly,beta}
                        set Rust channel (default: stable)
  --target {llvm-ir,wasm,asm,mir,ast}
                        build for the target triple (default: ast)
  --disable-color       disable colors and styles for stderr (default: False)
```

## Example

Say you want to quick test some Rust code but your current machine doesn't have
the Rust compiler installed.

```rust
// test.rs
fn main() {
    for x in 1..5 {
        println!("{}", x);
    }
}
```

```bash
$ playground test.rs
   Compiling playground v0.0.1 (file:///playground)
    Finished dev [unoptimized + debuginfo] target(s) in 2.36s
     Running `target/debug/playground`
1
2
3
4
```

It reads your `test.rs` and passes it to http://play.rust-lang.org for compilation
and then returns stdout/stderr output on your terminal, which looks very alike to
`$ cargo run`.

## License

[![License](https://img.shields.io/github/license/ritiek/rust-without-rust.svg)](https://github.com/ritiek/rust-without-rust/blob/master/LICENSE)
