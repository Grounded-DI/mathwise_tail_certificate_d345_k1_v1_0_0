# Tail Certificate Proof

## Definitions

Let

\[
B=\{3^a:a\ge 1\}\cup\{4^b:b\ge 1\}\cup\{5^c:c\ge 1\}.
\]

Let \(\operatorname{SubSum}(B)\) be the set of all finite subset sums of distinct elements of \(B\).

Set

\[
C=80.
\]

## Initial finite prefix

Let

\[
F=B\cap[1,2187)
=\{3,4,5,9,16,25,27,64,81,125,243,256,625,729,1024\}.
\]

Then

\[
\sum_{f\in F} f=3236.
\]

The replay verifier exhaustively enumerates subset sums of \(F\) and confirms

\[
[80,3156]\subseteq \operatorname{SubSum}(F),
\]

where

\[
3156=3236-80.
\]

The same finite enumeration confirms

\[
79\notin \operatorname{SubSum}(B).
\]

Since every element of \(B\) greater than \(79\) is too large to appear in a representation of \(79\), this endpoint obstruction is finite.

## Propagation lemma

Let \(x\in B\) be a basis element with \(x\ge 2187\). Let

\[
T(x)=\sum_{\substack{b\in B\\ b<x}} b
\]

be the total of all earlier basis elements.

For \(q\in\{3,4,5\}\), the sum of the \(q\)-powers below \(x\) is at least

\[
\frac{x-q}{q-1}.
\]

Therefore

\[
T(x)\ge
\frac{x-3}{2}+\frac{x-4}{3}+\frac{x-5}{4}
=
\frac{13x-49}{12}.
\]

For \(x\ge 1957\),

\[
\frac{13x-49}{12}\ge x+159.
\]

Since every later basis element satisfies \(x\ge2187>1957\), we have

\[
T(x)\ge x+159.
\]

Equivalently,

\[
x\le T(x)-159=T(x)-2C+1.
\]

Now suppose a finite prefix \(P\subset B\) has total \(T\) and satisfies

\[
[80,T-80]\subseteq \operatorname{SubSum}(P).
\]

Let \(x\) be the next basis element. If \(x\le T-159\), then the translated interval

\[
x+[80,T-80]=[x+80,x+T-80]
\]

overlaps or touches the existing interval \([80,T-80]\), because

\[
x+80\le T-79.
\]

Thus

\[
[80,T+x-80]\subseteq \operatorname{SubSum}(P\cup\{x\}).
\]

Starting from the verified prefix \(F\), the propagation condition holds for every subsequent basis element. Hence the certified covered interval expands without bound.

Therefore

\[
[80,\infty)\subseteq \operatorname{SubSum}(B).
\]

Together with \(79\notin\operatorname{SubSum}(B)\), this proves

\[
C(\{3,4,5\},1)=80.
\]
