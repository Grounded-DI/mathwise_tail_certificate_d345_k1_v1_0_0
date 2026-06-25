# Release Notes v1.0.0

## Title

A Fixed Exact-Conductor Certificate for Subset Sums of Powers of 3, 4, and 5

## Result

This release certifies the fixed-case exact conductor

\[
C(\{3,4,5\},1)=80.
\]

## Certificate components

- Endpoint obstruction: \(79\notin\operatorname{SubSum}(B)\).
- Initial interval: \([80,3156]\subseteq\operatorname{SubSum}(F)\), where \(F=B\cap[1,2187)\).
- Infinite propagation: every later basis element satisfies the interval-overlap condition.

## Replay

```bash
python3 verify_tail_certificate_d345_k1.py
```

Expected final line:

```text
FINAL STATUS: PASS | EXACT_CONDUCTOR_PROVED
```

## Scope

Fixed case only: \(D=\{3,4,5\}\), \(k=1\).
