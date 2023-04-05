a_list = [100, 100, 100, 100, 100, 100, 100, 100,
          100, 100, 1000, 1000, 1000, 1000, 10, 10,
          10, 10, 10, 10, 10, 10, 10]

sum_manual = 0
for list_element in a_list:
    sum_manual += list_element

print(sum_manual)
print(sum(a_list))

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
        
print(content_ratings)

