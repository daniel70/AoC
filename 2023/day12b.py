import re
# ???.### 1,1,3


total = 0
def matcher(s: str, groups: list, count=0):
    global total
    s = s.strip(".")
    if not groups and not "#" in s:
        total += count
        return
    if s == "":
        return
    group = groups.pop(0)
    matches = re.finditer(f"^[\?|#]{{{group}}}[^#]", s)
    for match in matches:
        matcher(s[match.start() + 1:], groups, count+1)

matcher("???.###", [1, 1, 3])
print(total)