#!/usr/bin/env python3
hosts = open("hosts.txt")
hosts_file = hosts.read()
newhosts = open("hosts_adguard.txt", "xt")
newerhosts = hosts_file.replace("0.0.0.0 ", "||")
newesthosts = newerhosts.replace("\n", "^\n")
newhosts.write(str(newesthosts))
newhosts.close()
hosts.close()
