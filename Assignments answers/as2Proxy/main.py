import requests
import random
import csv

def parse_proxy_servers():
   f = open('raw.txt', 'r')
   s = f.read().split(sep='\n')
   f.close()

   proxy_servers = []
   prefix = 'http://'
   for i in range(len(s)):
      cur = s[i].split(',')
      ip_address = cur[0]
      port = cur[1][1:len(cur[1])-1]
      proxy_servers.append(prefix + ip_address + ":" + port)
   
   f = open('parsed.txt', 'w')
   result = ""
   for i in range(len(proxy_servers)):
      result += proxy_servers[i]
      if i != len(proxy_servers) - 1:
         result += '\n'

   f.write(result)
   f.close()


def get_proxy_servers():
   parse_proxy_servers()

   f = open('parsed.txt', 'r')
   proxy_servers = f.read().split('\n')
   f.close()

   return proxy_servers

def main():
   proxy_servers = get_proxy_servers()

   url = 'https://old.stat.gov.kz/api/juridical/counter/api/?bin=971240001315&lang=ru'

   cnt = 0
   f = open('working servers.txt', 'w')

   for i in range(2000, len(proxy_servers)):
      try:
         # proxy = random.choice(proxy_servers)
         # proxy = 'http://172.105.105.132:8080'
         proxy = proxy_servers[i]
         print(proxy)
         proxies = {
            'http': proxy,
            'https': proxy,
         }

         response = requests.get(url, proxies=proxies)
         print(response.status_code)

         if(response.status_code == 200):
            f.write(proxy + '\n')
      except Exception as e:
         print(e)

      cnt += 1
      if cnt % 100 == 0:
         print('cnt = ', cnt)

main()