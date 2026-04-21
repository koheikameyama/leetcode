# 1431. Kids With the Greatest Number of Candies

- **Difficulty**: Easy
- **Tags**: Array
- **URL**: <https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/>

## 問題概要

n人の子供がキャンディを持っている。各子供が持っているキャンディの数を表す配列 `candies` と、追加のキャンディ数 `extraCandies` が与えられる。

各子供に `extraCandies` を全部あげた場合、その子供が全員の中で最大（または同率最大）のキャンディ数を持てるかどうかを判定し、boolean の配列を返す。

**例:**
- 入力: `candies = [2,3,5,1,3]`, `extraCandies = 3`
- 出力: `[true,true,true,false,true]`

## 初回の解答の問題点

```python
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    return [item + extraCandies >= max(candies) for item in candies]
```

**問題点**: `max(candies)` をリスト内包表記の中で毎回呼び出している。

- `max(candies)` は O(n) の操作
- それを n 回繰り返すため、全体で **O(n²)** になってしまう

## 改善した解答

```python
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    mx = max(candies)
    return [candy + extraCandies >= mx for candy in candies]
```

**改善点**: `max(candies)` を先に一度だけ計算して変数に格納。

## プロの解答

```python
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    mx = max(candies)
    return [candy + extraCandies >= mx for candy in candies]
```

### なぜベストか

1. **最適な計算量**: max を一度だけ計算し、各要素を一度だけ走査
2. **シンプルで読みやすい**: リスト内包表記で意図が明確
3. **Pythonic**: 組み込み関数 `max()` とリスト内包表記を活用

### 面接での補足

- 「まず最大値を求め、各子供がその最大値に到達できるか判定する」という2ステップのアプローチを説明
- 最大値を先に計算することで計算量が O(n) になることを強調

## 計算量

- **時間計算量**: O(n) — max で1回走査 + リスト内包表記で1回走査
- **空間計算量**: O(n) — 結果のリストを格納

## 学んだこと

- リスト内包表記内で関数を呼ぶ場合、その関数が毎回評価されることに注意
- 不変の値（この場合 max）は事前に計算して変数に格納すべき
- 小さな最適化だが、O(n²) → O(n) は大きな差になりうる
