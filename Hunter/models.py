from django.db import models



class HttpEndpoint(models.Model):
    endpoint_url = models.CharField(max_length=200)
    ssl_two_zero_enbled = models.BooleanField()
    ssl_two_zero_supported_cipher_list = models.CharField(max_length=10000)
    ssl_three_zero_enbled = models.BooleanField()
    ssl_three_zero_supported_cipher_list = models.CharField(max_length=10000)
    tls_one_zero_enbled = models.BooleanField()
    tls_one_zero_supported_cipher_list = models.CharField(max_length=10000)
    tls_one_one_enbled = models.BooleanField()
    tls_one_one_supported_cipher_list = models.CharField(max_length=10000)
    tls_one_two_enbled = models.BooleanField()
    tls_one_two_supported_cipher_list = models.CharField(max_length=10000)
    final_score_percentage = models.IntegerField()
    
    def set_endpoint_url(self,endpoint_url):
        self.endpoint_url = endpoint_url 
    
    def get_endpoint_url(self):
        return self.endpoint_url
    
    def set_ssl_two_zero_enbled(self,enabled):
        self.ssl_two_zero_enbled = enabled
    
    def get_ssl_two_zero_enbled(self):
        return self.ssl_two_zero_enbled
    
    def set_ssl_two_zero_supported_cipher_list(self,supported_cipher_list):
        self.ssl_two_zero_supported_cipher_list = supported_cipher_list
    
    def set_ssl_three_zero_enbled(self,enabled):
        self.ssl_three_zero_enbled = enabled
    
    def get_ssl_three_zero_enbled(self):
        return self.ssl_three_zero_enbled
    
    def set_ssl_three_zero_supported_cipher_list(self,supported_cipher_list):
        self.ssl_three_zero_supported_cipher_list = supported_cipher_list
    
    def set_tls_one_zero_enbled(self,enabled):
        self.tls_one_zero_enbled = enabled
    
    def get_tls_one_zero_enbled(self):
        return self.tls_one_zero_enbled
    
    def set_tls_one_zero_supported_cipher_list(self,supported_cipher_list):
        self.tls_one_zero_supported_cipher_list = supported_cipher_list
    
    def set_tls_one_one_enbled(self,enabled):
        self.tls_one_one_enbled = enabled

    def get_tls_one_one_enbled(self):
        return self.tls_one_one_enbled
        
    def set_tls_one_one_supported_cipher_list(self,supported_cipher_list):
        self.tls_one_one_supported_cipher_list = supported_cipher_list
    
    def set_tls_one_two_enbled(self,enabled):
        self.tls_one_two_enbled = enabled
    
    def get_tls_one_two_enbled(self):
        return self.tls_one_two_enbled 
        
    def set_tls_one_two_supported_cipher_list(self,supported_cipher_list):
        self.tls_one_two_supported_cipher_list = supported_cipher_list
    
    def set_final_score_percentage(self,final_score_percentage):
        self.final_score_percentage = final_score_percentage
   
    