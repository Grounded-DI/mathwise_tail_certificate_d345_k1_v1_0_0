# Reviewer Checklist

1. Run the replay verifier:

```bash
python3 verify_tail_certificate_d345_k1.py
```

2. Confirm the finite prefix:

```text
F = {3,4,5,9,16,25,27,64,81,125,243,256,625,729,1024}
sum(F) = 3236
```

3. Confirm the initial interval:

```text
[80,3156] subset SubSum(F)
```

4. Confirm endpoint obstruction:

```text
79 notin SubSum(B)
```

5. Check the propagation inequality:

```text
T(x) >= (13x-49)/12 >= x+159, for x >= 1957.
```

6. Confirm the first later basis element is:

```text
2187 > 1957.
```

7. Confirm the interval-overlap condition:

```text
x <= T - 159
```

extends `[80,T-80]` to `[80,T+x-80]`.

8. Confirm no general theorem is claimed.
