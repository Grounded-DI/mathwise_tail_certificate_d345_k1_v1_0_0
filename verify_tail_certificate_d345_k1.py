#!/usr/bin/env python3
"""
verify_tail_certificate_d345_k1.py

Replay verifier for the fixed-case tail certificate

    [80, infinity) subset SubSum({3^a:a>=1} U {4^b:b>=1} U {5^c:c>=1})

and endpoint obstruction

    79 notin SubSum(B).

This verifier checks:
1. The finite initial interval [80, 3156] using the finite prefix B_<2187.
2. The endpoint obstruction 79 not representable.
3. The deterministic propagation inequality for every subsequent basis element.

No probabilistic search is used.
No result for any other D or k is asserted.
"""

from __future__ import annotations

BASES = (3, 4, 5)
C = 80
ENDPOINT_OBSTRUCTION = 79
TAIL_START = 2187
INEQUALITY_THRESHOLD = 1957


def powers_less_than(limit: int, bases=BASES) -> list[int]:
    out: list[int] = []
    for q in bases:
        x = q
        while x < limit:
            out.append(x)
            x *= q
    return sorted(set(out))


def powers_leq(limit: int, bases=BASES) -> list[int]:
    out: list[int] = []
    for q in bases:
        x = q
        while x <= limit:
            out.append(x)
            x *= q
    return sorted(set(out))


def subset_sum_witnesses(items: list[int]) -> dict[int, tuple[int, ...]]:
    witnesses: dict[int, tuple[int, ...]] = {0: ()}
    for x in items:
        # Freeze current state so x is used at most once.
        for s, w in list(witnesses.items()):
            ns = s + x
            if ns not in witnesses:
                witnesses[ns] = w + (x,)
    return witnesses


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    initial_basis = powers_less_than(TAIL_START)
    initial_total = sum(initial_basis)
    initial_interval_end = initial_total - C

    expected_initial_basis = [3, 4, 5, 9, 16, 25, 27, 64, 81, 125, 243, 256, 625, 729, 1024]
    assert_true(initial_basis == expected_initial_basis, "Unexpected initial basis below 2187.")
    assert_true(initial_total == 3236, "Unexpected initial-prefix total.")
    assert_true(initial_interval_end == 3156, "Unexpected initial interval endpoint.")

    witnesses = subset_sum_witnesses(initial_basis)

    missing_initial = [n for n in range(C, initial_interval_end + 1) if n not in witnesses]
    assert_true(not missing_initial, f"Initial interval failure; first missing values: {missing_initial[:20]}")

    endpoint_basis = powers_leq(ENDPOINT_OBSTRUCTION)
    endpoint_witnesses = subset_sum_witnesses(endpoint_basis)
    assert_true(
        ENDPOINT_OBSTRUCTION not in endpoint_witnesses,
        "Endpoint obstruction failed: 79 was represented."
    )

    # Propagation lemma.
    #
    # Let x be any later basis element x >= 2187.
    # For q in {3,4,5}, the sum of q-powers below x is at least (x-q)/(q-1).
    # Therefore the previous-prefix total T(x) is at least
    #
    #   (x-3)/2 + (x-4)/3 + (x-5)/4 = (13x - 49)/12.
    #
    # If x >= 1957, then (13x - 49)/12 >= x + 159.
    # Since every later basis element has x >= 2187 > 1957, T(x) >= x+159.
    # This is exactly the interval-overlap condition:
    #
    #   x <= T(x) - 159 = T(x) - 2*C + 1.
    #
    # Thus if [C, T- C] is covered by a prefix, adding x extends coverage to
    # [C, T+x-C].
    lhs = 13 * INEQUALITY_THRESHOLD - 49
    rhs = 12 * (INEQUALITY_THRESHOLD + 159)
    assert_true(lhs >= rhs, "Threshold arithmetic failed at x=1957.")
    assert_true(TAIL_START > INEQUALITY_THRESHOLD, "Tail start does not exceed inequality threshold.")

    first_later_x = TAIL_START
    assert_true(
        first_later_x <= initial_total - (2 * C - 1),
        "First propagation step fails interval-overlap condition."
    )

    print("TAIL CERTIFICATE REPLAY: PASS")
    print("D = {3,4,5}, k = 1")
    print("B = {3^a:a>=1} union {4^b:b>=1} union {5^c:c>=1}")
    print("INITIAL BASIS BELOW 2187:", initial_basis)
    print("INITIAL PREFIX TOTAL:", initial_total)
    print("INITIAL INTERVAL CERTIFIED: [80, 3156]")
    print("ENDPOINT OBSTRUCTION: 79 NOT REPRESENTABLE")
    print("PROPAGATION LEMMA: PASS")
    print("INFINITE TAIL CERTIFIED: [80, infinity) subset SubSum(B)")
    print("COMBINED RESULT: C({3,4,5},1) = 80")
    print("FINAL STATUS: PASS | EXACT_CONDUCTOR_PROVED")


if __name__ == "__main__":
    main()
