#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


from sslyze.concurrent_scanner import ConcurrentScanner, PluginRaisedExceptionScanResult
from sslyze.plugins.utils.certificate_utils import CertificateUtils
from sslyze.plugins.certificate_info_plugin import CertificateInfoScanCommand
from sslyze.plugins.session_renegotiation_plugin import SessionRenegotiationScanCommand
from sslyze.server_connectivity import ServerConnectivityInfo, ServerConnectivityError
from sslyze.ssl_settings import TlsWrappedProtocolEnum
from sslyze.synchronous_scanner import SynchronousScanner
from sslyze.plugins.openssl_cipher_suites_plugin import Tlsv10ScanCommand, Tlsv11ScanCommand, Tlsv12ScanCommand, Tlsv13ScanCommand

if __name__ == '__main__':
    # Setup the server to scan and ensure it is online/reachable
    hostname = 'smtp.gmail.com'
    try:
        server_info = ServerConnectivityInfo(hostname=u'www.ebay.com')
        server_info.test_connectivity_to_server()
    except ServerConnectivityError as e:
        # Could not establish an SSL connection to the server
        raise RuntimeError('Error when connecting to {}: {}'.format(hostname, e.error_msg))

# Run one scan command synchronously to list the server's TLS 1.0 cipher suites
print(u'\nRunning one scan command synchronously...')
synchronous_scanner = SynchronousScanner()
command = Tlsv10ScanCommand()
scan_result = synchronous_scanner.run_scan_command(server_info, command)
print('All the TLS 1.0 Ciphers: \n')
print('\n Accepted Cipher List: \n')
for cipher in scan_result.accepted_cipher_list:
    print(u'    {}'.format(cipher.name))
print('\n Preffered Cipher =: \n')
print(u'    {}'.format(scan_result.preferred_cipher.name))
    
    
command = Tlsv11ScanCommand()
scan_result = synchronous_scanner.run_scan_command(server_info, command)
print('\nAll the TLS 1.1 Ciphers: \n')
print('\n Accepted Cipher List: \n')
for cipher in scan_result.accepted_cipher_list:
    print(u'    {}'.format(cipher.name))
print('\n Preffered Cipher =: \n')
print(u'    {}'.format(scan_result.preferred_cipher.name))   
    
command = Tlsv12ScanCommand()
scan_result = synchronous_scanner.run_scan_command(server_info, command)
print('\nAll the TLS 1.2 Ciphers: \n')
print('\n Accepted Cipher List: \n')
for cipher in scan_result.accepted_cipher_list:
    print(u'    {}'.format(cipher.name))
print('\n Preffered Cipher =: \n')
print(u'    {}'.format(scan_result.preferred_cipher.name))

command = Tlsv13ScanCommand()
scan_result = synchronous_scanner.run_scan_command(server_info, command)
print('\nAll the TLS 1.3 Ciphers: \n')
print('\n Accepted Cipher List: \n')
for cipher in scan_result.accepted_cipher_list:
    print(u'    {}'.format(cipher.name))
print('\n Preffered Cipher =: \n')
print(u'    {}'.format(scan_result.preferred_cipher.name))