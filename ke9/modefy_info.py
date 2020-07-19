from ke9.login_function import login

import requests

s = requests.session()
a = login(s)
print(a)


