st = 'X-DSPAM-Confidence:0.8475'
s = st.find(':')
print(float(st[s+1:]))
