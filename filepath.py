import os


st = open('st.txt','w')
st.write('Hello')
st.close()


with open('st.txt','r') as f:
    print(f.read())