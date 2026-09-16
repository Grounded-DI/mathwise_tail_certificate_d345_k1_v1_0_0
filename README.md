# Fixed Exact-Conductor Certificate for `{3,4,5}`, `k=1`

This package contains a replayable certificate for the fixed-case theorem

```text
C({3,4,5},1) = 80
```

For `B = {3^a : a >= 1} ∪ {4^b : b >= 1} ∪ {5^c : c >= 1}`, it establishes that every integer `n >= 80` is a subset sum of distinct elements of `B`, while `79` is not representable.

## Recorded result

Running `python3 verify_tail_certificate_d345_k1.py` produces:

- `TAIL CERTIFICATE REPLAY: PASS`;
- finite initial interval `[80,3156]` certified from the basis below `2187`;
- endpoint obstruction `79 NOT REPRESENTABLE`;
- propagation lemma `PASS`;
- infinite tail `[80, infinity)` certified;
- `FINAL STATUS: PASS | EXACT_CONDUCTOR_PROVED`.

## Evidence and replay

The package preserves the theorem statement, proof, finite witnesses, nonrepresentables, verifier source, replay log, manifest, checksums, reviewer checklist, and scope documents. The exact finite prefix used by the verifier is listed in `INITIAL_BASIS_BELOW_2187.txt`; the complete witness interval is in `INITIAL_INTERVAL_WITNESSES_80_3156.txt`.

## Scope

This is a fixed case only: `D={3,4,5}`, `k=1`. It does not claim a general BEGL theorem, results for other triples or other `k`, a density/asymptotic/classification theorem, or independent third-party acceptance.

`SHA256SUMS.txt` is a recorded package manifest; a checksum establishes the identity of the hashed bytes, not the mathematical truth of every statement in those bytes. Reviewers should run the verifier and inspect the proof and scope files.

## License

The repository includes a license file. Consult it before redistribution.
