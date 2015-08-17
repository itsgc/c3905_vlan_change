# c3905_vlan_change
This is a simple script used to push configuration to Cisco 3905 Phones.

There is no way to set a static VLAN ID for Voice traffic from Cisco Communications Manager. It is expected that endpoints will operate in an LLDP/CDP compatible network.

The value can only be set directly from the Phone UI or from a CLI interface over telnet. The CLI interface is derivative and not based on Cisco IOS. The syntax is simple but custom for this product.

This makes the change cumbersome when needed on a large number of phones.

I recently dealt with a network in which a portion was mainly built from legacy Allied Telesyn switch that have no LLDP/CDP support. 

In such a scenario, phones are unable to "learn" from their upstream switch what VLAN are they supposed to tag voice traffic with. Connecting a phone to such a network would result in being unable to call or even register to the PBX.

This script manually sets the VLAN id. I used it to set this parameter on 100 phones in less than 2 minutes.

The hardcoded value we're setting will be respected only as long as the endpoint is not connected to an LLDP/CDP-aware switch. A VLAN ID set through these protocols will override a manual setting every time.

The script learns target hosts through a text file, one IP per line.

Credentials to logon to the phone are stored in credentials.yml. Only one set of credentials for all targets, sorry.
