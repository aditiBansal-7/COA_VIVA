# 🚀 Dockerized PostgreSQL Setup – COAA VIVA

This repository documents the steps taken to set up and interact with a PostgreSQL database using Docker as part of the **Container Orchestration and Automation** coursework.

---

## 🔧 Commands Used and Their Purpose

### 1. Create a Docker Network
```bash
docker network create my_postgres_network_aditi
🔹 Purpose: Created a custom bridge network so that containers can communicate securely and efficiently.

2. Pull PostgreSQL Image from Docker Hub
bash
Copy
Edit
docker pull postgres
🔹 Purpose: Pulled the official PostgreSQL image to run the database container locally.

3. Run PostgreSQL Container
bash
Copy
Edit
docker run --name my_postgres_aditi_coa \
--network my_postgres_network_aditi \
-e POSTGRES_USER=Aditi \
-e POSTGRES_PASSWORD=secret \
-e POSTGRES_DB=testdb \
-p 5433:5432 \
-d postgres
🔹 Purpose:

Launched a PostgreSQL container with:

Aditi as the username

secret as the password

testdb as the default database

Exposed port 5432 (Postgres default) on local port 5433

Connected it to the custom Docker network

4. Access PostgreSQL Shell Inside Container
bash
Copy
Edit
docker exec -it my_postgres_aditi_coa psql -U Aditi -d testdb
🔹 Purpose: Entered the PostgreSQL shell inside the container to run SQL commands interactively.

5. SQL Operations
sql
Copy
Edit
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO passengers (name, location) VALUES
('Aditi', 'Udaipur'), 
('Shardul', 'Udaipur'), 
('Ananya', 'Dehradun');

SELECT * FROM passengers;
🔹 Purpose:

Created a passengers table

Inserted sample records

Queried the table to verify successful insertion

✅ Outcome
Successfully ran a PostgreSQL database inside a Docker container and performed database operations through the containerized environment.
