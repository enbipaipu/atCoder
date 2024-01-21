s = input()
s_list = list(s)  # が余分

a_count = s_list.count("A")
b_count = s_list.count("B")
c_count = s_list.count("C")

str_ = ("A" * a_count) + ("B" * b_count) + ("C" * c_count)

if str_ == s:
    print("Yes")
else:
    print("No")
