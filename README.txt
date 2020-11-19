Hello,

In order to run this application build Docker image
Powershell: Get-Content Dockerfile | docker build . --tag bl_friendship --no-cache
bash: docker build . --tag bl_friendship --no-cache < Dockerfile 
after build just run built image:
docker run bl_friendship

Application is available in localhost:5000

I had no time to write addidional files to run tests, but with project installed locally it is possible to perform tests.
Best Regards,
Bartosz Lipiński
