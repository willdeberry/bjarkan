# Copyright 2016 GetWellNetwork, Inc., BSD copyright and disclaimer apply

import dbus.service

class Agent(dbus.service.Object):
    """
    This is the code that deals with generating a PIN code if needed by the bluetooth device
    we are connecting to in order to complete the authentication handshake.
    """
    AGENT_INTERFACE = 'org.bluez.Agent1'
    exit_on_release = True

    def set_exit_on_release(self, exit_on_release):
        self.exit_on_release = exit_on_release

    @dbus.service.method(AGENT_INTERFACE)
    def Release(self):
        if self.exit_on_release:
            mainloop.quit()

    @dbus.service.method(AGENT_INTERFACE, in_signature = 'os')
    def DisplayPinCode(self, device, pincode):
        print('DisplayPinCode ({}, {})'.format(device, pincode))

    @dbus.service.method(AGENT_INTERFACE, in_signature = 'ou')
    def RequestConfirmation(self, device, passkey):
        print('RequestConfirmation ({}, {})'.format(device, passkey))

