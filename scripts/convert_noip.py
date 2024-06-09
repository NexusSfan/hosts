#!/usr/bin/env python3
hosts = open("hosts.txt")
hosts_file = hosts.read()
newhosts = open("hosts_noip.txt", "xt")
newhosts.write(hosts_file.replace("0.0.0.0 ", ""))
newhosts.close()
hosts.close()
