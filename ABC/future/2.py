s, t = map(str, input().split())
s_parts = s.strip('/').split('/')
t_parts = t.strip('/').split('/')
i = 0

if s == '/':
    s_parts = []
if t == '/':
    t_parts = []

#print(f"{s_parts} {t_parts}")

while i < min(len(s_parts), len(t_parts)) and s_parts[i] == t_parts[i]:
    i += 1

cd_up = len(s_parts) - i
cd_down = len(t_parts) - i

print(cd_up + cd_down) 