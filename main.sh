curl https://codeload.github.com/redis/redis/tar.gz/refs/tags/7.0-rc1 -o 7.0-rc1.tar.gz

tar -xzvf ./7.0-rc1.tar.gz

cd ./redis-7.0-rc1

make

cd ..

python move_binary.py