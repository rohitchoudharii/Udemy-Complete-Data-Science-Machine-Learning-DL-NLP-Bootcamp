st = {1, 2, 3, 4, 5}
print(st)
print(type(st))

st = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(st)

# Adding elements to a set
st.add(6)
print(st)
st.add(6)
print(st)

# Removing elements from a set
st.remove(6)
print(st)
st.discard(6)
print(st)

el = st.pop()
print(el)
print(st)

st.clear()
print(st)


# Set Membership
st = {1, 2, 3, 4, 5}
print(4 in st)

# Set Operations
st1 = {1, 2, 3, 4, 5}
st2 = {4, 5}
print(st1.union(st2))
print(st1.intersection(st2))
# print(st1.intersection_update(st2))
print(st1.difference(st2))
# print(st1.difference_update(st2))
print(st1.symmetric_difference(st2))
# print(st1.symmetric_difference_update(st2))
print(st2.issubset(st1))
print(st1.issuperset(st2))
print(st1.isdisjoint(st2))
