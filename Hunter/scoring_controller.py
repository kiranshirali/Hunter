from .models import HttpEndpoint
from .tls_controller import test_endpoint_for_tls_settings
from .tls_controller import test_endpoint_for_secure_headers



def test_and_score_endpoint(httpEndpoint):
    
    httpEndpoint = test_endpoint_for_tls_settings(httpEndpoint)
    httpEndpoint = test_endpoint_for_secure_headers(httpEndpoint)
    
    final_score_percentage = 100
    
    if httpEndpoint.get_ssl_two_zero_enbled() is True:
        final_score_percentage = final_score_percentage - 25
    if httpEndpoint.get_ssl_three_zero_enbled() is True:
        final_score_percentage = final_score_percentage - 25
    if httpEndpoint.get_tls_one_zero_enbled() is True:
        final_score_percentage = final_score_percentage - 5
    if httpEndpoint.get_tls_one_one_enbled() is True:
        final_score_percentage = final_score_percentage - 5
    if httpEndpoint.get_tls_one_two_enbled() is not True:
        final_score_percentage = final_score_percentage - 5
    
    httpEndpoint.set_final_score_percentage(final_score_percentage)
    
    return httpEndpoint