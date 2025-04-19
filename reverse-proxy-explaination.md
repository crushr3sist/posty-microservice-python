our nginx config is paramount for a "sane" microservice backend. this configuration could be called an api-gateway as its the gateway for all of the other services such as logic or auth or more (analytics or logs) who knows but this is how we enter our backend.

- reverse proxy -> nginx sits between the client and backend services, forwarding requests
- microservices gateway -> it directs traffic to different microservces based on request paths (/auth/, /logic/)
- cors middleware -> it enables CORS headers to allow cross-origin communication between the frontend and the microservces.

as these services are dockerised, we're using the hostname: host.docker.internal to refer to the docker hostname as the services are dockerised.

upstreams to posty-auth and posty-logic to make requests to backend services
handle cors to allow request from different origins.
impliments reverse proxying to route requests from /auth/ to posty_auth and /logic/ to posty_logic.

this configuration allows for one unified entry point, making it easier for the frontend to make queries by a single hostname and port, and since nginx is a load-balancer along with reverse proxy engine, it does 2 for 1. backend services remain hidden from direct access, improving security and maintainability.
