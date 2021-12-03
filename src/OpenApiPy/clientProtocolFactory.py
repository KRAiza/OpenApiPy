#!/usr/bin/env python

from twisted.internet.protocol import ClientFactory

class ClientProtocolFactory(ClientFactory):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.client = kwargs['client']
        self.numberOfMessagesToSendPerSecond = self.client.numberOfMessagesToSendPerSecond
    def buildProtocol(self, addr):
        protocol = super().buildProtocol(addr)
        return protocol
    def connected(self, protocol):
        self.client._connected(protocol)
    def disconnected(self, reason):
        self.client._disconnected(reason)
    def received(self, message):
        self.client._received(message)