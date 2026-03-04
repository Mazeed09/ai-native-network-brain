"""Mininet SDN topology for telecom lab experiments.

Creates a simple edge-cloud topology with controllable link attributes.
"""

from mininet.cli import CLI
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController


def build_topology() -> Mininet:
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, link=TCLink)

    controller = net.addController("c0", ip="127.0.0.1", port=6653)
    edge_sw = net.addSwitch("s1")
    core_sw = net.addSwitch("s2")

    ue1 = net.addHost("ue1", ip="10.0.0.1/24")
    ue2 = net.addHost("ue2", ip="10.0.0.2/24")
    edge_node = net.addHost("edge1", ip="10.0.0.10/24")
    cloud_node = net.addHost("cloud1", ip="10.0.0.100/24")

    net.addLink(ue1, edge_sw, bw=50, delay="20ms", loss=0.1)
    net.addLink(ue2, edge_sw, bw=50, delay="25ms", loss=0.3)
    net.addLink(edge_node, edge_sw, bw=200, delay="3ms", loss=0.0)
    net.addLink(edge_sw, core_sw, bw=100, delay="8ms", loss=0.2)
    net.addLink(core_sw, cloud_node, bw=500, delay="30ms", loss=0.1)

    net.build()
    controller.start()
    edge_sw.start([controller])
    core_sw.start([controller])
    return net


if __name__ == "__main__":
    network = build_topology()
    print("[mininet] Topology built. Use CLI for experiments.")
    CLI(network)
    network.stop()
