Django_Tastypie_OAuth
=====================

Built the API's using https://github.com/toastdriven/django-tastypie, providing OAuth authentication for the same using Leah Culver's Python-OAuth2 and David's Django-OAuth-Plus

Step 1: Register the consumer
        Once the consumer is registered, consumer key and consumer secret is given. These values are random generated strings.
        For example, we will assume
        consumer_key:key and consumer_secret:secret. 

Step 2: Request for an unauthorized request token
        For these the following parameters have to be sent in a GET request:
        oauth_consumer_key: *The consumer_key obtained from consumer registration*
        oauth_signature_method: *This will be 'PLAINTEXT'*
        oauth_signature: 
        oauth_version:  *This will have value '1.0'*
        oauth_timestamp: *Current time*
        oauth_nonce: *Random generated string*
        oauth_callback: *Any callback url*
        scope: *Name of the resource, one is trying to access*
        
        To illustrate with an example, the url would look somewhat like this:
        /oauth/request_token/?oauth_version=1.0&oauth_nonce=3a2fc01d88c298dcd4021ce67674f815&oauth_timestamp=1354901582&
        oauth_consumer_key=key&oauth_signature_method=PLAINTEXT&oauth_signature=secret%26
        &oauth_callback=http://wwstay.com&scope=booking
        
        This will download a text file, containing the oauth_token_key and oauth_token_secret.
        
Step 3: Authorization
        For these the following parameters have to be sent in a GET request:
        oauth_token: *The value of the oauth_token_key obtained from above*
        oauth_callback: *The url to hit after authorization*
        
        To illustrate with an exmaple, the url would look something like this:
        /oauth/authorize/?oauth_token=856b178d67bc4aa4831d840edea5dee4&oauth_callback=http://wwstay.com
        
        If successful, it will return http-status='200'
        
Step 4: Obtain Access Token
        For these the following parameters have to be sent in a GET request:
        oauth_consumer_key: *The consumer_key obtained from consumer registration*
        oauth_signature_method: *This will be 'PLAINTEXT'*
        oauth_signature: 
        oauth_version:  *This will have value '1.0'*
        oauth_timestamp: *Current time*
        oauth_nonce: *Random generated string*
        oauth_token: 
        oauth_verifier:
        scope: *Name of resource to be accessed*
        
        To illustrate with an example, the url would look something like this:
        /oauth/access_token/?oauth_version=1.0&
        oauth_nonce=28f57b81befba9de5143a10f17b31299&oauth_timestamp=1354901826&
        oauth_consumer_key=key&oauth_token=856b178d67bc4aa4831d840edea5dee4&
        oauth_signature_method=PLAINTEXT&oauth_signature=secret%26QrqavVKt8wZMFmja
        &oauth_verifier=verifier&scope=booking
        
Step 5: Access the Resources 
        For these the following parameters have to be sent in a GET request:
        oauth_consumer_key: *The consumer_key obtained from consumer registration* 
        oauth_signation_method: *This will be PLAINTEXT*
        oauth_signature:
        oauth_version:  *This will have value '1.0'*
        oauth_timestamp: *Current time*
        oauth_nonce: *Random generated string*
        oauth_token: 
        format: *The format will be 'json'*
        
        To illustrate with an example, the url would look something like this:
        /api/v1/booking/1/?oauth_version=1.0&oauth_nonce=b5141207b10cba58b91171f61dbf691c&oauth_timestamp=1354901992
        &oauth_consumer_key=key&format=json&oauth_token=50a5a8bacff04f05a710842c3b3d3f35
        &oauth_signature_method=PLAINTEXT&oauth_signature=secret%2526dykZBCXqMNSP4k3
        
        And this will display the resources in json format!!! :)
