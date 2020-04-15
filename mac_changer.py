#!/usr/bin/env python3

import subprocess as sub
import optparse as opt
def get_argument():
    parser = opt.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC address Assign")
    (options , arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-]Please specify MAC address, use --help for more info.")
    return options
def mac_changer(interface,new_mac):
    print("[+]Changing MAC address for ", interface, " to ", new_mac)
    sub.call(["ifconfig", interface, "down"])
    sub.call(["ifconfig", interface, "hw", "ether", new_mac])
    sub.call(["ifconfig", interface, "up"])
    print("[+]Your current MAC address is: ",new_mac)


(options) = get_argument()
mac_changer(options.interface,options.new_mac)


