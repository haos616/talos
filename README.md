Setup Nginx
-----------

```
proxy_cache_path /var/cache/nginx/auth_cache/ levels=1:2 keys_zone=auth_cache:1m max_size=100m use_temp_path=off;

map $http_authorization $custom_http_authorization  {
    "~*^Basic " "";
    default $http_authorization;
}
proxy_set_header AUTHORIZATION $custom_http_authorization;

server {
    server_name your-host.name;
    listen 80;

    auth_request /talos-auth/;
    auth_request_set $cookie $upstream_http_set_cookie;
    add_header Set-Cookie $cookie;

    location = /talos-auth/ {
        internal;
        proxy_pass https://talos-auth-domain.com/;
        proxy_pass_request_body off;
        proxy_method GET;

        proxy_cache auth_cache;
        proxy_cache_lock on;
        proxy_cache_key "$http_authorization $cookie_talos_sessionid";
        proxy_cache_valid 10m;
        
        proxy_set_header Content-Length "";
        proxy_set_header X-Original-HOST $host;
    }

    location /fake-webhook/ {
        auth_request off;
        proxy_pass http://example.com;
    }

    location / {
        proxy_pass http://backend;
    }

}
```
