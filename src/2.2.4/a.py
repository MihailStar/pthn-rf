# Задача A

# g=lambda m,k,s:sorted(map(lambda p:p["name"],filter(lambda p:p[k]==m(s,key=lambda p:p[k])[k],s)))
g=lambda m,k,s:sorted(p["name"] for p in (p for p in s if p[k]==m(p[k] for p in s)))
get_people_with_min_age=lambda s:g(min,"age",s)
get_people_with_max_age=lambda s:g(max,"age",s)
get_people_with_min_height=lambda s:g(min,"height",s)
get_people_with_max_height=lambda s:g(max,"height",s)
get_people_with_min_weight=lambda s:g(min,"weight",s)
get_people_with_max_weight=lambda s:g(max,"weight",s)
