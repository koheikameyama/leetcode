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
