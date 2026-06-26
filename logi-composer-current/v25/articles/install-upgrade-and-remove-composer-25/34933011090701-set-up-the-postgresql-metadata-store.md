---
title: " Set Up the PostgreSQL Metadata Store"
id: 34933011090701
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011090701--Set-Up-the-PostgreSQL-Metadata-Store
updated_at: 2026-05-26T22:07:26Z
---

#  Set Up the PostgreSQL Metadata Store

# Set Up the PostgreSQL Metadata Store

The instructions to set up PostgreSQL as Composer's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

* [PostgreSQL Setup for CentOS Environments](#PostgreS)
* [PostgreSQL Setup for Ubuntu Environments](#PostgreS2)

## PostgreSQL Setup for CentOS Environments

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

1. Add the PostgreSQL Yum repository to CentOS by running this command calling the appropriate PostgreSQL version:

   sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86\_64/pgdg-redhat-repo-latest.noarch.rpm
2. Install the PostgreSQL client and server packages by running these commands:

   sudo yum -y install epel-release yum-utils
   sudo yum-config-manager --enable pgdg12
   sudo yum install postgresql12-server postgresql12
3. After installation, initialize the PostgreSQL database:

   sudo /usr/pgsql-12/bin/postgresql12-setup initdb
4. Start and enable the PostgreSQLmicroservice:

   sudo systemctl enable --now postgresql-12
5. Confirm that the service started without errors:

   sudo systemctl status postgresql-12

   If necessary, start it:

   sudo systemctl start postgresql-12
6. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service:

   sudo firewall-cmd --add-service=postgresql --permanent
   sudo firewall-cmd --reload
7. If the PostgreSQL database is operating in a cluster, repeat steps 3-6 for each instance of the database.
8. Set up the PostgreSQL Admin user and password:

   sudo su - postgres
   ~]$ psql -c "alter user postgres with password 'StrongPassword'"
   ALTER ROLE

## PostgreSQL Setup for Ubuntu Environments

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

1. If this is a new server instance, update your current system packages:

   sudo apt update
   sudo apt -y install vim bash-completion wget
   sudo apt -y upgrade

   A reboot is necessary after an upgrade.

   sudo reboot
2. Import the GPG key and add the appropriate PostgreSQL version repository to your Ubuntu machine. Run the following commands:

   wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add
   echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb\_release -cs`-pgdg main" |sudo tee /etc/apt/sources.list.d/pgdg.list

   The added repository contains many different packages and third-party add-ons, including: `postgresql-client`, `postgresql`, `libpq-dev`, `postgresql-server-dev`, and `pgadmin packages`.
3. Update the package list and install the PostgreSQL server and client packages:

   sudo apt update
   sudo apt -y install postgresql-12 postgresql-client-12

   The PostgreSQL microservice is started and will start with every system reboot.
4. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service port:

   sudo ufw allow 5432/tcp
5. Test the PostgreSQL connection.

   1. During installation, a user named `postgres` is created automatically with full superadmin access to your entire PostgreSQL instance. Before you switch to this account, your logged in system user should have sudo privileges:

      sudo su - postgres
   2. Replace the `postgres` password with a strong password:

      psql -c "alter user postgres with password 'StrongAdminP@ssw0rd'"
   3. Start PostgreSQL using this command.

      $ psql
   4. Get connection details as shown below.

      postgres=# \conninfo
      You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
   5. Create a test database called `mytestdb` to see if everything is working.

      postgres=# CREATE DATABASE mytestdb;
      CREATE DATABASE
      postgres=# CREATE USER mytestuser WITH ENCRYPTED PASSWORD 'MyStr0ngP@SS';
      CREATE ROLE
      postgres=# GRANT ALL PRIVILEGES ON DATABASE mytestdb to mytestuser;
      GRANT

      You can list the created databases by running:

      postgres=# \l
   6. Connect to your test database.

      postgres-# \c mytestdb
      You are now connected to database "mytestdb" as user "postgres".
