docker-compose up --build
docker-compose build
docker scan
docker-compose run --rm frontend sh -c "npm install -g create-react-app && create-react-app react-project --template typescript"
docker-compose up