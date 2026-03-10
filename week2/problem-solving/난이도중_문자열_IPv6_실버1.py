# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

ip_list = input().split(":")
print(ip_list)
if len(ip_list) > 8:
    ip_list.remove('')
opt = 8 - len(ip_list)
org = ''

if '' in ip_list:
    for _ in range(opt):
        x = ip_list.index('')
        ip_list.insert(x, '')
        
for ip in ip_list:
    org_ip = "0" * (4-len(ip)) + ip
    org += org_ip + ":"

print(org[:-1])
        