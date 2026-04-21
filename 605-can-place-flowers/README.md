# 605. Can Place Flowers

- **Difficulty**: Easy
- **Tags**: Array, Greedy
- **URL**: <https://leetcode.com/problems/can-place-flowers/>

## 問題概要

花壇（`flowerbed`）が 0（空き）と 1（植えてある）の配列で与えられる。隣り合うマスに花を植えてはいけないルールのもとで、`n` 本の花を追加で植えられるかを判定する。

## 初回の解答の問題点

```python
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    listLen = len(flowerbed)
    addFlowers = 0
    for i, v in enumerate(flowerbed):
        pV = 0
        nV = 0
        if v == 0:
            if i > 0:
                pV = flowerbed[i - 1]
            if i < listLen - 1:
                nV = flowerbed[i + 1]
            if pV == 0 and nV == 0:
                addFlowers += 1
                flowerbed[i] = 1
    return addFlowers >= n
```

**問題点：**

1. **変数名が分かりにくい**: `pV`, `nV`, `listLen` などの略語が読みづらい
2. **冗長な初期化**: `pV = 0`, `nV = 0` を毎回設定し、条件に応じて上書きしている
3. **早期リターンがない**: すでに `n` 本植えられたのにループを続ける

## 改善した解答

```python
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left_empty = i == 0 or flowerbed[i - 1] == 0
            right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
```

**改善点：**

1. **条件の一行化**: `or` を使って境界条件と値チェックをまとめた
2. **意味のある変数名**: `left_empty`, `right_empty` で意図が明確
3. **早期リターン**: `n` 本植えたら即座に `True` を返す

## プロの解答

```python
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    f = [0] + flowerbed + [0]  # 番兵を追加
    for i in range(1, len(f) - 1):
        if f[i - 1] == f[i] == f[i + 1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0
```

**なぜベストか：**

- **番兵（Sentinel）パターン**: 配列の両端に `0` を追加することで、境界条件の分岐が不要になる
- **連鎖比較**: `f[i-1] == f[i] == f[i+1] == 0` という Python らしい書き方
- **カウントダウン方式**: `n` を減らしていき `n <= 0` で判定。追加変数不要

**面接での補足：**

- 「番兵を使うと境界条件の処理がシンプルになりますが、追加の空間 O(n) を使います」
- 「元の配列を変更したくない場合はコピーを作るか、植えた位置を別途管理する方法もあります」

## 計算量

| | 時間 | 空間 |
|---|---|---|
| 初回・改善版 | O(n) | O(1) |
| 番兵版 | O(n) | O(n) |

## 学んだこと

- **番兵パターン**: 配列の端に仮の値を追加して、境界条件を簡略化するテクニック
- **Python の連鎖比較**: `a == b == c` は `a == b and b == c` と同じ
- **早期リターン**: 条件を満たしたら即座に返すことでコードの見通しが良くなる
