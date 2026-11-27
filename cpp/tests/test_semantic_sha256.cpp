#include <cassert>
#include <string>

#include "lobby/SemanticSha256.hpp"

int main() {
    using tft::semantic::sha256_hex;
    assert(sha256_hex("") ==
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855");
    assert(sha256_hex("abc") ==
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
    assert(sha256_hex("The quick brown fox jumps over the lazy dog") ==
        "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592");
    return 0;
}
