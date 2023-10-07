import base64

ceshme = [
    'a', 
    'b', 
    'c', 
    'd', 
    'e', 
    'f', 
    'g', 
    'h', 
    'i', 
    'j', 
    'k', 
    'l', 
    'm', 
    'n', 
    'o', 
    'p', 
    'q', 
    'r', 
    's', 
    't', 
    'u', 
    'v', 
    'w', 
    'x', 
    'y', 
    'z'
    ]
netije = [
    'LzEtMDEv', 
    'LzMtMjAv', 
    'LzMtMzEv', 
    'LzYtMTY1Lw==', 
    'LzQtOTg5Lw==', 
    'LzctNzc2Lw==', 
    'LzAtMzEyLw==', 
    'LzItNDEyLw==', 
    'LzItMzk5Lw==', 
    'LzQtMjM0Lw==', 
    'LzMtMzQ1Lw==', 
    'LzY3LTEyMzk3OC8=', 
    'LzQ1Mi0xMzUxNS8=', 
    'LzcxMjYzLTMyMTY1MS8=', 
    'LzI0NTctOTcxMjUv', 
    'LzI0NTYtMzU2Nzgv', 
    'LzI0NTYtMzU2Nzkv', 
    'LzY1NDgtMzg1ODMzOC8=', 
    'LzIzNDUtMjQ5NTc2Lw==', 
    'LzU2NC01MjM0NTM3MjYv', 
    'LzI0Njc1LTYzNDc4Lw==', 
    'LzE3NjMtMTk4NzQ1Ni8=', 
    'LzE3NjMtMTk4NzQ1OC8=', 
    'LzE3NjMtMTk4NzQ2MS8=', 
    'LzYxMi0xNDM3Ny8=', 
    'LzY0NTM4LTM0ODU2OTgv'
]

berlen = input('Cheshme giriz: ')

for i in range(len(ceshme)):
    if(berlen == ceshme[i]):
        result = base64.b64decode(netije[i])
        print(result)
        break
