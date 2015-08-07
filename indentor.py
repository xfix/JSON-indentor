#!/usr/bin/python2
f=open("raw.txt")
text=f.read()
istack=[]
n=0
s=0
i=0
st=""
text=text.replace("\n{","{")
for c in text:
    if c=='\n':
        print st
        st=""
        i=1
        while i<=s:
            st=st+" "
            i=i+1
        n=0;
    elif not(c=='{' or c=='}' or c=='[' or c==']' or c==','):
        n=n+1
        st=st+c
    elif c=='}' or c==']':
        print st
        st=""
        i=1
        while i<=s:
            st=st+" "
            i=i+1
        print st+c
        st=""
        s=istack.pop()
        i=1
        while i<=s:
            st=st+" "
            i=i+1
        n=0
    elif c=='{' or c=='[':
        istack.append(s)
        s=n+istack[-1]
        print st+c
        st=""
        i=1
        while i<=s:
            st=st+" "
            i=i+1
        n=0
    elif c==',':
        print st+c
        st=""
        i=1
        while i<=s:
            st=st+" "
            i=i+1
        n=0
            
        
        
