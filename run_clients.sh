   #!/bin/bash

# Número de clientes que deseas crear
num_clients=100
# Ruta al archivo JAR
jar_file="client.jar"

run_client() {
  random_number1=$(shuf -i 1000000-9999999 -n 1)
  random_number2=$(shuf -i 1000000-9999999 -n 1)
  (echo "$random_number1"; echo "$random_number2"; echo "exit") | java -jar "$jar_file"

}

for ((i = 1; i <= num_clients; i++)); do
  run_client &
done

wait

