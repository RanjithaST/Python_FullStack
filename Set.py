subjects={"Maths":100,"Science":90,"Biology":100,"Chemistry":95}
print(subjects)

sub=dict()
sub["Maths"]=98
sub["Science"]=89
sub["Social"]=76
print(sub)
# {'Maths': 100, 'Science': 90, 'Biology': 100, 'Chemistry': 95}
# {'Maths': 98, 'Science': 89, 'Social': 76}

key=["Math","Science","Kannda","History"]#count of keys and values should match or else values will get ignored
value=[90,78,90,81]
sub=dict(zip(key,value))
print(sub)#{'Math': 90, 'Science': 78, 'History': 90}
for key,value in sub.items():
    print(f"{key}:{value}")
# Math:90
# Science:78
# Kannda:90
# History:81