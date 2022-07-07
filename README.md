# Module_8

 MySQL  localhost:33060+ ssl  pysports  SQL > create table teams ( players varchar(255), teams varchar(255) );
Query OK, 0 rows affected (0.0470 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > show tables;
+--------------------+
| Tables_in_pysports |
+--------------------+
| players            |
| teams              |
+--------------------+
2 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > create user 'pysports_user'@'localhost' identified with mysql_native_password by 'MySQL8IsGreat!';
Query OK, 0 rows affected, 1 warning (0.0295 sec)
Warning (code 4058): 1 factor authentication method does not match against authentication policy. Please refer @@authentication_policy system variable.
 MySQL  localhost:33060+ ssl  pysports  SQL > Grant all privileges on pysports.* TO 'pysports_user'@'localhost';
Query OK, 0 rows affected (0.0074 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > drop user if exists 'pysports-user'@'localhost';
Query OK, 0 rows affected, 1 warning (0.0102 sec)
Note (code 3162): Authorization ID 'pysports-user'@'localhost' does not exist.
 MySQL  localhost:33060+ ssl  pysports  SQL > drop user if exists 'pysports_user'@'localhost';
Query OK, 0 rows affected (0.0252 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > create Table team (
                                           -> team_id INT nOT NULL auto_increment,
                                           -> team_name Varchar(75) NOT NULL,
                                           -> mascot varchar(75) NOT NULL,
                                           -> primary KEY(team_id)
                                           -> );
Query OK, 0 rows affected (0.0551 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > create table player (
                                           -> player_id INT NOT NULL auto_increment,
                                           -> first_name Varchar(75) NOT NULL,
                                           -> last_name Varchar(75) NOT NULL,
                                           -> team_id INT NOT NULL,
                                           -> primary key(player_id),
                                           -> constraint fk_team
                                           -> foreign key(team_id)
                                           -> reference team(team_id)
                                           -> );
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'reference team(team_id)
)' at line 9
 MySQL  localhost:33060+ ssl  pysports  SQL > create table player ( player_id INT NOT NULL auto_increment, first_name Varchar(75) NOT NULL, last_name Varchar(75) NOT NULL, team_id INT NOT NULL, primary key(player_id), constraint fk_team foreign key(team_id) references team(team_id) );
Query OK, 0 rows affected (0.0522 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > insert into team(team_name, mascot)
                                           -> values('Team Gandalf', 'White Wizard');
Query OK, 1 row affected (0.0274 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > source/home/rkrasso/csd/csd-310/module_7/db_init.sql
                                           ->
                                           -> use pysports;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'source/home/rkrasso/csd/csd-310/module_7/db_init.sql
use pysports' at line 1
 MySQL  localhost:33060+ ssl  pysports  SQL > drop table if exists player;
Query OK, 0 rows affected (0.0367 sec)
 MySQL  localhost:33060+ ssl  pysports  SQL > select team_id from team where team_name = "Team Sauron')
                                           "> ^C
 MySQL  localhost:33060+ ssl  pysports  SQL > select team_id from where team_name = 'Team Sauron'
                                           -> ^C
 MySQL  localhost:33060+ ssl  pysports  SQL >
