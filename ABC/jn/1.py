from collections import defaultdict

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.char_count = defaultdict(int)
        self.current_chars = set()
        self.valid_symbols = set("@$%")
        self.min_length = self.length + 1

    def is_valid_password(self):
        """パスワードが条件を満たしているかチェック"""
        lowercase_count = len([c for c in self.current_chars if c.isalpha() and c.islower()])
        has_symbol = any(c in self.valid_symbols for c in self.current_chars)
        return lowercase_count >= 5 and has_symbol

    def update_char_count(self, char, increment=True):
        """文字のカウントを更新"""
        if increment:
            self.char_count[char] += 1
            if char.isalpha() and char.islower() or char in self.valid_symbols:
                self.current_chars.add(char)
        else:
            self.char_count[char] -= 1
            if self.char_count[char] == 0:
                self.current_chars.discard(char)

    def find_worst_password(self):
        """最悪のパスワードの長さを見つける"""
        left = 0
        for right in range(self.length):
            self.update_char_count(self.password[right])

            while self.is_valid_password():
                self.min_length = min(self.min_length, right - left + 1)
                self.update_char_count(self.password[left], increment=False)
                left += 1

        return self.min_length if self.min_length <= self.length else -1

def worst_pass(s):
    analyzer = PasswordAnalyzer(s)
    return analyzer.find_worst_password()

# 入力から結果を出力
s = input()
print(worst_pass(s))