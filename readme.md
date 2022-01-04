##Install Docker for Ubuntu 
 - sudo apt install docker.io
 - sudo apt install docker-compose
 
### Why we using docker?
- Selenium needs to be `chromedriver`, `edge.exe` etc. But every computer have a different configuration that's why we need to use a docker-compose file 'cause if we'r running on the docker-compose we can get a stable system.   

### How to run this project?
- `pip install -r requirements.txt`
- `cd build && docker-compose up`
- open new tab and run; 
  - If you run `behave --junit` code on the terminal, you can get a report about the test-cases, but sometimes we get error because of the `pokedex website` 
  - And another option is the run test-cases with tags;
    - for smoke: `behave --tags=smoke`
    - for button visibility and functionality: `behave --tags=button`
    - for pokemon visibility and functionality`behave --tags=pokes`
    - for search`behave --tags=search`
    - `behave --tags=`

