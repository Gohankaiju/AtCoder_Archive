def worst_pass(s):
    from collections import defaultdict

    n = len(s)
    ans = n + 1
    left = 0
    char_cnt = defaultdict(int)
    now_chars = set()
    symbols = set("@$%")

    #調べる範囲を左端から広げていく
    for right in range(n):
        char_cnt[s[right]] += 1
        #文字が英小文字
        if s[right].isalpha() and s[right].islower():
            now_chars.add(s[right])
        #文字が使える特殊記号
        if s[right] in symbols:
            now_chars.add(s[right])
        #now_chars の中に　小文字のアルファベットが5種類以上である and　少なくとも一つ以上記号が存在する
        while len([c for c in now_chars if c.isalpha() and c.islower()]) >= 5 and any(c in symbols for c in now_chars):
            ans = min(ans, right - left + 1)
            char_cnt[s[left]] -= 1
            #文字の出現回数がゼロの場合要素を削除
            if char_cnt[s[left]] == 0:
                now_chars.discard(s[left])
            #左端を一つ右に移動
            left += 1

    return ans if ans <= n else -1

# 入力から結果を出力
s = input()
print(worst_pass(s))
