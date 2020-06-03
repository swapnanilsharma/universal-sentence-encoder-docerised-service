# universal-sentence-encoder-docerised-service

#### Commands to run
   - sudo docker-compose up -d

#### API contract: 
    - ENDPOINT: http://<server-ip-address>:2222/getvector
    - METHOD: POST
    - HEADER: {"Content-Type": "application/json"}
    - BODY: {"searchString": <list/array of string>}; e.g. {"searchString": ["hello world", "hi world"]}
    - RESPONSE STRUCTURE: a 2D array/list/matrix of size Nx512 where N is size of the array passed in the BODY section
