import random

kuji = ["大吉","中吉","小吉"]

kuji.append("凶")
kuji.append("大凶")
kuji.append("趙大吉")

# print(kuji)

# print("追加後のおみくじ一覧:",kuji)
print("追加後のおみくじ一覧:",", ".join(kuji))
print("ここからランダムでおみくじを引きます")

results = []
results_daikichi = 0

for i in range(5):
    result = random.choice(kuji)
    print(f"{i+1}回目の結果: {result}")
    results.append(result)

    if result == "大吉":
        results_daikichi += 1

print("---- 抽選結果まとめ ----")
print(results)
print(f"大吉回数: {results_daikichi}")