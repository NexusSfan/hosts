#!/usr/bin/env python3
hosts = open("hosts.txt")
newhosts = open("hosts_noip.txt", "xt")
newhosts.write(hosts.replace("0.0.0.0 ", ""))
newhosts.close()
hosts.close
