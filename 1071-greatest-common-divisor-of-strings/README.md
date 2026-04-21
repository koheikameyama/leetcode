# 1071. Greatest Common Divisor of Strings

- Difficulty: Easy
- Tags: Math, String
- URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/

## 問題

2つの文字列 `str1` と `str2` が与えられる。文字列 `t` が `str1` と `str2` の両方を「割り切る」とき、`t` を共通因子と呼ぶ。最大の共通因子を返す。存在しない場合は空文字を返す。

文字列 `t` が文字列 `s` を「割り切る」とは、`s = t + t + ... + t`（`t` を1回以上繰り返した形）であること。

## 初回の解答の問題点

- str2の最小構成要素を探る方針は正しいが、str1とstr2の**両方**を割り切る**最大**の文字列を探す必要がある
- 愚直に探索すると計算量が増える

## 改善した解答

```python
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
```

- `str1 + str2 == str2 + str1` でGCDが存在するかを一発判定
- 存在するなら、長さのGCDがそのまま答えの長さになる

## プロの解答

上記の解答がすでにベスト。さらに1行で書くと：

```python
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""
```

**なぜこれがベストか:**

- 数学的な洞察を活かして O(n+m) で解ける
- `str1 + str2 == str2 + str1` という条件が、両文字列が同じ基本単位の繰り返しかを判定する
- 標準ライブラリの `math.gcd` を活用

**面接での補足ポイント:**

- 「なぜ `str1 + str2 == str2 + str1` で判定できるのか」を説明できるようにする
  - 両方の文字列が同じ「基本単位」の繰り返しなら、どちらを先に足しても同じ結果になる
  - 逆に、この条件を満たさなければ共通の基本単位は存在しない
- `gcd` を自分で実装できるか聞かれる可能性もある（ユークリッドの互除法）

## 計算量

- 時間: O(n + m) — 文字列の結合と比較に O(n+m)、gcd計算は O(log(min(n,m)))
- 空間: O(n + m) — 文字列結合時に新しい文字列を生成

## 学んだこと

- 文字列のGCD問題は、数値のGCDの考え方がそのまま適用できる
- `str1 + str2 == str2 + str1` は「両方が同じ基本単位の繰り返しか」を判定する強力な条件
- Python 2では `fractions.gcd`、Python 3では `math.gcd` を使う
- 問題を数学的に捉え直すと、シンプルな解法が見つかることがある
