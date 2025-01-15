from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI

class SRv6SDWAN(Topo):
    def build(self):
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(s1, s2)

def run():
    topo = SRv6SDWAN()
    net = Mininet(topo=topo, controller=RemoteController, switch=OVSSwitch)
    net.start()

    # Run CLI
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
