# 1768. Merge Strings Alternately

- Difficulty: Easy
- Tags: Two Pointers, String
- URL: <https://leetcode.com/problems/merge-strings-alternately/>

## 問題

2つの文字列 `word1` と `word2` を交互に1文字ずつマージする。片方が長い場合は残りをそのまま末尾に追加する。

## 初回の解答の問題点

- `word1List`, `word2List` - listに変換しているが未使用
- `0 <= index` - `range()` は必ず0以上なので不要な条件
- `result +=` - 文字列はイミュータブルなのでループ内で毎回新しいオブジェクトを生成して非効率

## 改善した解答

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return ''.join(result)
```

- `list.append` + `''.join()` で効率的な文字列結合
- 不要な変数・条件を削除

## プロの解答

```python
from itertools import zip_longest

class Solution(object):
    def mergeAlternately(self, word1, word2):
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
```

**なぜこれがベストか:**

- `zip_longest` が長さの差を吸収してくれるので、if分岐が不要
- ジェネレータ式で中間リストを作らず省メモリ
- 1行で意図が明確に伝わる — 「2つの文字列を交互にマージする」がそのままコードになっている
- 標準ライブラリを適切に使いこなしていることを示せる

**面接での補足ポイント:**

- 「`zip_longest` を使わずに書けますか？」と聞かれたら改善版（Two Pointers）を出せるようにしておく
- 標準ライブラリに頼るだけでなく、基礎的なアルゴリズムも理解していることを示す

## 計算量

- 時間: O(n + m) — n, m はそれぞれ word1, word2 の長さ。全解法で同じ
- 空間: O(n + m) — 結果の文字列分

## 学んだこと

- Pythonの文字列はイミュータブル。ループ内 `+=` は O(n^2) になりうる。`list` + `join` が定石
- `itertools.zip_longest` で長さの異なるイテラブルを fillvalue で埋めて同時走査できる
- 標準ライブラリを知っていれば、自分でロジックを書かずに済むケースが多い
- 面接では「シンプルな解法」と「ライブラリを使った解法」の両方を出せると強い
