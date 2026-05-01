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

## collections

### `deque`

両端からの追加・削除が高速（O(1)）なキュー。リストの `pop(0)` は O(n) だが、`deque.popleft()` は O(1)。

```python
from collections import deque

q = deque([1, 2, 3])
q.popleft()  # O(1) で先頭削除
# 1

q.append(4)  # 末尾に追加
# deque([2, 3, 4])

q.appendleft(0)  # 先頭に追加
# deque([0, 2, 3, 4])
```

**シグネチャ:** `deque([iterable[, maxlen]])`

**引数:**

- `iterable`: 初期値として設定するイテラブル（省略可）
- `maxlen`: 最大長を指定すると、超過分は自動的に削除される（省略可）

**ポイント:**

- リストの `pop(0)` は O(n)（全要素をシフトするため）
- キューのような操作（FIFO）には必ず `deque` を使う
- 両端操作が多い場合にも有効（例: スライディングウィンドウ）

- Docs: https://docs.python.org/3/library/collections.html#collections.deque
- 出会った問題: [345. Reverse Vowels of a String](345-reverse-vowels-of-a-string/)

## string

### `''.join(list)` で文字列を結合

ループ内で `+=` を使った文字列連結は、毎回新しい文字列オブジェクトを作成するため非効率（O(n²)）。`''.join()` を使うと O(n) で済む。

```python
# ❌ 遅い（O(n²)）
result = ''
for char in ['a', 'b', 'c']:
    result += char

# ✅ 速い（O(n)）
result = ''.join(['a', 'b', 'c'])
# 'abc'
```

**シグネチャ:** `separator.join(iterable)`

**引数:**

- `separator`: 区切り文字（例: `','`, `' '`, `''`）
- `iterable`: 結合したい文字列のイテラブル

**ポイント:**

- Python の文字列は immutable なので、`+=` は毎回新しいオブジェクトを作る
- リスト内包表記と組み合わせるとさらに強力（例: `''.join([c.upper() for c in s])`）

- Docs: https://docs.python.org/3/library/stdtypes.html#str.join
- 出会った問題: [345. Reverse Vowels of a String](345-reverse-vowels-of-a-string/)

## set

### set で高速検索（O(1)）

`in` 演算を頻繁に行う場合、リストよりも set の方が圧倒的に速い（O(1) vs O(n)）。

```python
# ❌ 遅い（O(n) × ループ回数 = O(n²)）
vowels = 'aeiou'
if char in vowels:  # 文字列を毎回線形探索
    ...

# ✅ 速い（O(1) × ループ回数 = O(n)）
vowels = set('aeiou')
if char in vowels:  # ハッシュテーブルで即座に検索
    ...
```

**ポイント:**

- set はハッシュテーブルで実装されているため、検索が O(1)
- 重複を許さないため、ユニークな要素を扱う場合にも便利
- 順序は保証されない（Python 3.7+ の dict とは異なる）

- Docs: https://docs.python.org/3/library/stdtypes.html#set
- 出会った問題: [345. Reverse Vowels of a String](345-reverse-vowels-of-a-string/)

## パターン

### Two Pointers（両端から探索）

配列の両端からポインタを動かし、条件を満たす要素を探索・処理するパターン。

```python
left, right = 0, len(arr) - 1

while left < right:
    if condition(arr[left], arr[right]):
        # 処理
        left += 1
        right -= 1
    elif ...:
        left += 1
    else:
        right -= 1
```

**使いどころ:**

- 配列の両端から探索したい場合（例: palindrome判定、反転、ペア探索）
- ソート済み配列で2つの要素の和を探す（例: Two Sum II）
- In-place で配列を操作したい場合

**ポイント:**

- 1パスで処理できるため、時間計算量が O(n)
- 空間計算量も O(1)（追加のデータ構造不要）
- 類似問題: "Valid Palindrome", "Container With Most Water", "3Sum"

- 出会った問題: [345. Reverse Vowels of a String](345-reverse-vowels-of-a-string/)
