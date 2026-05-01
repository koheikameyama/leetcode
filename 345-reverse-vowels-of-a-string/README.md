# 345. Reverse Vowels of a String

**Difficulty:** Easy
**Tags:** Two Pointers, String
**URL:** https://leetcode.com/problems/reverse-vowels-of-a-string

## 問題概要

文字列内の母音（a, e, i, o, u）のみを逆順にして返す。大文字小文字は区別する。

**例:**
- Input: `s = "hello"` → Output: `"holle"`
- Input: `s = "leetcode"` → Output: `"leotcede"`

## 初回の解答の問題点

[initial.py](initial.py) の問題点：

1. **`pop(0)` が非効率**: リストの先頭削除は O(n) の操作。全体でループするため O(n²) になる
2. **文字列連結 `+=` が非効率**: Python では毎回新しい文字列を作成するため、累積コストが高い
3. **不要なリスト作成**: `reverse_vowels` リストを別途作成しているため、空間計算量が増加

```python
# 問題のあるコード
revese_vowels = [char for char in s_list if char in vowels][::-1]
resolve = ''
for item in s_list:
    if item in vowels:
        resolve += revese_vowels.pop(0)  # O(n) × n回 = O(n²)
    else:
        resolve += item  # 文字列連結も非効率
```

## 改善した解答

[solution.py](solution.py)

```python
class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # set で検索を O(1) に
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # 左から母音を探す
            if s_list[left] not in vowels:
                left += 1
                continue

            # 右から母音を探す
            if s_list[right] not in vowels:
                right -= 1
                continue

            # 両方が母音ならswap
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)
```

**改善点:**
1. **Two Pointers で1パス**: 左右から同時に探索し、母音を見つけたらswap
2. **In-place swap**: 追加のリスト作成が不要
3. **set で高速検索**: `in` 演算が O(1)
4. **`''.join()` で効率的な文字列生成**: 文字列連結より高速

## プロの解答

上記の Two Pointers 解答がベスト。

**なぜベストか:**
- 配列を1回走査するだけで完了（O(n)）
- 余計なメモリを使わない（元の配列を書き換えるのみ）
- コードが読みやすく、意図が明確

**面接での補足:**
- Two Pointers パターンは「配列の両端から探索」する典型的なテクニック
- 類似問題: "Valid Palindrome", "Container With Most Water"
- Pythonの文字列は immutable なので、`list()` に変換してから操作する必要がある

## 計算量

| | 初回の解答 | Two Pointers |
|---|---|---|
| **時間計算量** | O(n²) | O(n) |
| **空間計算量** | O(n) | O(n) |

※ 空間計算量は両方とも O(n)（文字列をリストに変換するため）

## 学んだこと

1. **Two Pointers パターン**: 配列の両端から探索する典型的なアプローチ
2. **`pop(0)` は遅い**: リストの先頭削除は O(n)。キューのような操作には `collections.deque` を使う
3. **文字列連結は `join()` で**: ループ内での `+=` は避ける
4. **set で高速検索**: `in` 演算を頻繁に行う場合は set に変換（O(1) 検索）
