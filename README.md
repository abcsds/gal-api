# Gal
A quick HTTP server for the Galactica model: https://github.com/paperswithcode/galai

Build the Docker image using the Dockerfile with the command `docker build . -t gal`

Run a container from the image with the command `docker run -p 5000:5000 gal`

Test with curl: `curl -X POST -d 'prompt=Event Related Potentials have been used before to classify emotions from facial expressions [START_REF]' http://localhost:5000/`