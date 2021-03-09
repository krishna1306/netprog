
from ncclient import manager
import xmltodict
import xml.dom.minidom

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

with manager.connect(host='sandbox-iosxe-latest-1.cisco.com', 
                        port=830, username='developer',password='C1sco12345', 
                        hostkey_verify=False,device_params={}, 
                        allow_agent=False,look_for_keys=False) as m:

                        #netconf_reply = m.get_config(source = 'running', filter = netconf_filter)


                        netconf_reply = m.get_config(source = 'running')

                        #print(netconf_reply.xml)
                        
                        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
                        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
                        #print(dir(m))
                        #print(help(m.get_config))

                         # Parse the returned XML to an Ordered Dictionary
                        netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]["interfaces"]


                        #print(netconf_data)
                        # Create a list of interfaces
                        #interfaces = netconf_data["interfaces"][1]

                        #print(interfaces)
                        # for interface in interfaces:
                        #     print("Interface {} enabled status is {}".format(
                        #         interface[1],
                        #         interface[1]
                        #         )
                        #     )