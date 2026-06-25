# mathwise_tail_certificate_d345_k1_v1_0_0
This package contains a replayable certificate for the fixed-case theorem C({3,4,5},1) = 80.

# A Fixed Exact-Conductor Certificate for Subset Sums of Powers of 3, 4, and 5

This package contains a replayable certificate for the fixed-case theorem

```text
C({3,4,5},1) = 80.
```

Equivalently, every integer `n >= 80` is representable as a subset sum of distinct elements of

```text
B = {3^a : a >= 1} union {4^b : b >= 1} union {5^c : c >= 1},
```

and `79` is not representable.

## Contents

```text
README.md
THEOREM_STATEMENT.md
TAIL_CERTIFICATE_PROOF.md
paper_section_d345_exact_conductor.tex
verify_tail_certificate_d345_k1.py
TAIL_CERTIFICATE_REPLAY_PASS.log
INITIAL_BASIS_BELOW_2187.txt
INITIAL_INTERVAL_WITNESSES_80_3156.txt
NONREPRESENTABLES_BELOW_80.txt
RELEASE_NOTES_v1.0.0.md
SCOPE_LIMITATIONS.md
REVIEWER_CHECKLIST.md
NO_OVERCLAIM_AUDIT.md
SHA256SUMS.txt
PACKAGE_MANIFEST.md
```

## Replay

Run:

```bash
python3 verify_tail_certificate_d345_k1.py
```

Expected status:

```text
TAIL CERTIFICATE REPLAY: PASS
INFINITE TAIL CERTIFIED: [80, infinity) subset SubSum(B)
COMBINED RESULT: C({3,4,5},1) = 80
FINAL STATUS: PASS | EXACT_CONDUCTOR_PROVED
```

## Proof structure

The proof has two parts.

1. A finite initial interval check using

```text
F = B cap [1,2187)
  = {3,4,5,9,16,25,27,64,81,125,243,256,625,729,1024}.
```

The sum of this finite prefix is `3236`, and the verifier checks that every integer in

```text
[80,3156]
```

is a subset sum of `F`.

2. A deterministic propagation lemma.

For any later basis element `x >= 2187`, the previous-prefix total `T(x)` satisfies

```text
T(x) >= (x-3)/2 + (x-4)/3 + (x-5)/4 = (13x-49)/12 >= x + 159.
```

This is the exact overlap condition needed to extend a covered interval

```text
[80,T-80]
```

to

```text
[80,T+x-80].
```

Because the prefix totals diverge, this proves the infinite tail `[80,infinity)`.

The endpoint obstruction `79 notin SubSum(B)` is checked by finite exhaustive enumeration, since no basis element greater than `79` can appear in a representation of `79`.

## Scope limitations

This package proves only the fixed case

```text
D = {3,4,5}, k = 1.
```

It does not claim:

- a general BEGL theorem;
- results for other triples `D`;
- results for `k != 1`;
- a density theorem;
- an asymptotic theorem;
- a classification theorem;
- independent third-party acceptance.

## License

Choose the repository license before release. Suggested:

- verifier source code: MIT License;
- paper, tables, logs, README, and documentation: CC BY 4.0.
