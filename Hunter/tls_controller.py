#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


from sslyze.concurrent_scanner import ConcurrentScanner, PluginRaisedExceptionScanResult
from sslyze.plugins.utils.certificate_utils import CertificateUtils
from sslyze.plugins.certificate_info_plugin import CertificateInfoScanCommand
from sslyze.plugins.session_renegotiation_plugin import SessionRenegotiationScanCommand
from sslyze.server_connectivity import ServerConnectivityInfo, ServerConnectivityError
from sslyze.server_connectivity import ServerConnectivityInfo
from sslyze.ssl_settings import TlsWrappedProtocolEnum
from sslyze.utils.http_request_generator import HttpRequestGenerator
from sslyze.utils.http_response_parser import HttpResponseParser
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding
from sslyze.synchronous_scanner import SynchronousScanner
from sslyze.plugins.openssl_cipher_suites_plugin import Sslv20ScanCommand, Sslv30ScanCommand, Tlsv10ScanCommand, Tlsv11ScanCommand, Tlsv12ScanCommand, Tlsv13ScanCommand
from sslyze.plugins.http_headers_plugin import HttpHeadersScanCommand 
from .models import HttpEndpoint

#if __name__ == '__main__':
   
def test_endpoint_for_tls_settings(httpEndpoint):
    
    # Setup the server to scan and ensure it is online/reachable
    hostname = httpEndpoint.get_endpoint_url()
    try:
        server_info = ServerConnectivityInfo(hostname=hostname)
        server_info.test_connectivity_to_server()
    except ServerConnectivityError as e:
        # Could not establish an SSL connection to the server
        raise RuntimeError('Error when connecting to {}: {}'.format(hostname, e.error_msg))
    
    
    # Run one scan command synchronously to list the server's SSL 2.0 cipher suites
    print(u'\nRunning one scan command synchronously...')
    synchronous_scanner = SynchronousScanner()
    command = Sslv20ScanCommand()
    scan_result = synchronous_scanner.run_scan_command(server_info, command)
    print('All the TLS 1.0 Ciphers: \n')
    print('\n Accepted Cipher List: \n')
    accepted_cipher_suite_list = []
    for cipher in scan_result.accepted_cipher_list:
        print(u'    {}'.format(cipher.name))
        accepted_cipher_suite_list.append(cipher.name)
    
    if len(scan_result.accepted_cipher_list) > 0:
        httpEndpoint.set_ssl_two_zero_enbled(True)
        httpEndpoint.set_ssl_two_zero_supported_cipher_list(accepted_cipher_suite_list)
    else:
        httpEndpoint.set_ssl_two_zero_enbled(False)
    #if scan_result.preferred_cipher is not None:
    #    print('\n Preffered Cipher =: \n')
    #    print(u'    {}'.format(scan_result.preferred_cipher.name))  
 
     # Run one scan command synchronously to list the server's SSL 3.0 cipher suites
    print(u'\nRunning one scan command synchronously...')
    synchronous_scanner = SynchronousScanner()
    command = Sslv30ScanCommand()
    scan_result = synchronous_scanner.run_scan_command(server_info, command)
    print('All the TLS 1.0 Ciphers: \n')
    print('\n Accepted Cipher List: \n')
    accepted_cipher_suite_list = []
    for cipher in scan_result.accepted_cipher_list:
        print(u'    {}'.format(cipher.name))
        accepted_cipher_suite_list.append(cipher.name)
    
    if len(scan_result.accepted_cipher_list) > 0:
        httpEndpoint.set_ssl_three_zero_enbled(True)
        httpEndpoint.set_ssl_two_three_supported_cipher_list(accepted_cipher_suite_list)
    else:
        httpEndpoint.set_ssl_three_zero_enbled(False)
    #if scan_result.preferred_cipher is not None:
    #    print('\n Preffered Cipher =: \n')
    #    print(u'    {}'.format(scan_result.preferred_cipher.name))  
 
 
     
    # Run one scan command synchronously to list the server's TLS 1.0 cipher suites
    print(u'\nRunning one scan command synchronously...')
    synchronous_scanner = SynchronousScanner()
    command = Tlsv10ScanCommand()
    scan_result = synchronous_scanner.run_scan_command(server_info, command)
    print('All the TLS 1.0 Ciphers: \n')
    print('\n Accepted Cipher List: \n')
    accepted_cipher_suite_list = []
    for cipher in scan_result.accepted_cipher_list:
        print(u'    {}'.format(cipher.name))
        accepted_cipher_suite_list.append(cipher.name)
    
    if len(scan_result.accepted_cipher_list) > 0:
        httpEndpoint.set_tls_one_zero_enbled(True)
        httpEndpoint.set_tls_one_zero_supported_cipher_list(accepted_cipher_suite_list)
    else:
        httpEndpoint.set_tls_one_zero_enbled(False)   
    #if scan_result.preferred_cipher is not None:
    #    print('\n Preffered Cipher =: \n')
    #    print(u'    {}'.format(scan_result.preferred_cipher.name))  
        
        
    command = Tlsv11ScanCommand()
    scan_result = synchronous_scanner.run_scan_command(server_info, command)
    accepted_cipher_suite_list = []
    for cipher in scan_result.accepted_cipher_list:
        print(u'    {}'.format(cipher.name))
        accepted_cipher_suite_list.append(cipher.name)
    
    if len(scan_result.accepted_cipher_list) > 0:
        httpEndpoint.set_tls_one_one_enbled(True)
        httpEndpoint.set_tls_one_one_supported_cipher_list(accepted_cipher_suite_list)
    else:
        httpEndpoint.set_tls_one_one_enbled(False)   
    #if scan_result.preferred_cipher is not None:
    #    print('\n Preffered Cipher =: \n')
    #    print(u'    {}'.format(scan_result.preferred_cipher.name))  
        
    command = Tlsv12ScanCommand()
    scan_result = synchronous_scanner.run_scan_command(server_info, command)
    accepted_cipher_suite_list = []
    for cipher in scan_result.accepted_cipher_list:
        print(u'    {}'.format(cipher.name))
        accepted_cipher_suite_list.append(cipher.name)
    
    if len(scan_result.accepted_cipher_list) > 0:
        httpEndpoint.set_tls_one_two_enbled(True)
        httpEndpoint.set_tls_one_two_supported_cipher_list(accepted_cipher_suite_list)
    else:
        httpEndpoint.set_tls_one_two_enbled(False)   
    #if scan_result.preferred_cipher is not None:
    #    print('\n Preffered Cipher =: \n')
    #    print(u'    {}'.format(scan_result.preferred_cipher.name))  
        
    return httpEndpoint       
    #command = HttpHeadersScanCommand()
    #scan_result = synchronous_scanner.run_scan_command(server_info, command)   
    #print(u'HttpHeadersScanResult {}'.format(scan_result.as_text()))

def  test_endpoint_for_secure_headers(httpEndpoint):
    
    
     # Setup the server to scan and ensure it is online/reachable
    hostname = httpEndpoint.get_endpoint_url()
    try:
        server_info = ServerConnectivityInfo(hostname=hostname)
        server_info.test_connectivity_to_server()
    except ServerConnectivityError as e:
        # Could not establish an SSL connection to the server
        raise RuntimeError('Error when connecting to {}: {}'.format(hostname, e.error_msg))
    
    hpkp_report_only = False

    # Perform the SSL handshake
    ssl_connection = server_info.get_preconfigured_ssl_connection()
    ssl_connection.connect()
    certificate_chain = [
         cryptography.x509.load_pem_x509_certificate(x509_cert.as_pem().encode('ascii'), backend=default_backend())
        for x509_cert in ssl_connection.ssl_client.get_peer_cert_chain()
    ]
    # Send an HTTP GET request to the server
    ssl_connection.write(HttpRequestGenerator.get_request(host=server_info.hostname))
    http_resp = HttpResponseParser.parse(ssl_connection)
    ssl_connection.close()

    if http_resp.version == 9:
        # HTTP 0.9 => Probably not an HTTP response
        raise ValueError('Server did not return an HTTP response')
    else:
        hsts_header = http_resp.getheader('strict-transport-security', None)
        x_frame_options_header = http_resp.getheader('x-frame-options', None)
        x_xss_protection_header  = http_resp.getheader('x-xss-protections', None)    
        content_security_policy_header = http_resp.getheader('Content-Security-Policy', None) 
        content_security_policy_report_only_header = http_resp.getheader('content-security-policy-report-only', None)       
        hpkp_header = http_resp.getheader('public-key-pins', None)
        expect_ct_header = http_resp.getheader('expect-ct', None)
        if hpkp_header is None:
            hpkp_report_only = True
            hpkp_header = http_resp.getheader('public-key-pins-report-only', None)

    # We do not follow redirections because the security headers must be set on the first page according to
    # https://hstspreload.appspot.com/:
    # "If you are serving an additional redirect from your HTTPS site, that redirect must still have the HSTS
    # header (rather than the page it redirects to)."
    
    if hsts_header is not None:
        httpEndpoint.set_hsts_enabled(True)
        if "includeSubDomains".lower() not in hsts_header.lower():
            httpEndpoint.set_hsts_issues("includeSubDomains is not set.")
        if "max-age".lower() not in hsts_header.lower():
            issueValue = httpEndpoint.set_hsts_issues()
            issueValue += "max-age is not set."
            httpEndpoint.set_hsts_issues(issueValue)
    if x_xss_protection_header is not None:
        httpEndpoint.set_x_xss_protection_enabled(True)
    if x_frame_options_header is not None:
        httpEndpoint.set_x_frame_options_enabled(True)
    if content_security_policy_header is not None:
        httpEndpoint.set_csp_enabled(True)
    
    
    print(hsts_header)
    #print(x_frame_options_header)
    #print(x_xss_protection_header)
    print(content_security_policy_header)
    #print(content_security_policy_report_only_header)
    #print(http_resp.getheaders())
    
    return httpEndpoint   
