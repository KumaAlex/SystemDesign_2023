def parse_proxy_servers():
   f = open('raw.txt', 'r')
   s = f.read().split(sep='\n')
   f.close()

   proxy_servers = []
   prefix = 'http://'
   for i in range(len(s)):
      cur = s[i].split('\t')
      proxy = prefix + cur[0] + ":" + cur[1]
      proxy_servers.append(proxy)


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
