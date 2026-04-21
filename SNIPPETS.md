# Snippets

LeetCodeで出会った「知らなかった関数・構文」のメモ。カテゴリ別・使いたい場面から逆引きできる形で整理する。

## itertools

### `zip_longest`

長さの異なるイテラブルを、最長のものに合わせて同時走査する。足りない要素は `fillvalue` で埋める。

```python
from itertools import zip_longest

list(zip_longest([1, 2, 3], ['x', 'y'], fillvalue='-'))
# [(1, 'x'), (2, 'y'), (3, '-')]
```

**シグネチャ:** `zip_longest(*iterables, fillvalue=None)`

**引数:**

- `*iterables`: まとめて走査したいイテラブルを可変長で受け取る。2つでも3つ以上でも可（例: `zip_longest(a, b, c)`）
- `fillvalue`: 短い側が尽きた後に埋めるための値。デフォルトは `None`。文字列連結なら `''`、数値加算なら `0` など、後続処理に合わせて指定する

**ポイント:**

- 通常の `zip()` は最短に合わせて停止するのに対し、`zip_longest` は最長に合わせる
- 2つの配列・文字列を交互に処理したい時に、長さの差を吸収できて if 分岐が不要になる

- Docs: https://docs.python.org/3/library/itertools.html#itertools.zip_longest
- 出会った問題: [1768. Merge Strings Alternately](1768-merge-strings-alternately/)

## math

### `gcd`

2つの整数の最大公約数（Greatest Common Divisor）を返す。

```python
from math import gcd

gcd(12, 8)   # 4
gcd(15, 25)  # 5
gcd(7, 3)    # 1（互いに素）
```

**シグネチャ:** `gcd(a, b)` (Python 3.9以降は `gcd(*integers)` で複数対応)

**引数:**

- `a`, `b`: 最大公約数を求めたい2つの整数。負の値も可（絶対値で計算される）
- Python 3.9以降は可変長引数で3つ以上の整数のGCDも一度に計算可能

**ポイント:**

- Python 2では `fractions.gcd`、Python 3では `math.gcd` を使う
- 文字列のGCD問題では、長さのGCDを取ることで解ける場合がある
- 内部的にはユークリッドの互除法で O(log(min(a,b))) で計算される
- `lcm(a, b) = a * b // gcd(a, b)` で最小公倍数も求められる（Python 3.9以降は `math.lcm` あり）

- Docs: https://docs.python.org/3/library/math.html#math.gcd
- 出会った問題: [1071. Greatest Common Divisor of Strings](1071-greatest-common-divisor-of-strings/)
