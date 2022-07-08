 CREATE TABLE player (
 player_id INT NOT NULL AUTO_INCREMENT,
 first_name VARCHAR(75) NOT NULL,
 last_name VARCHAR(75) NOT NULL,
 team_id INT NOT NULL,
 PRIMARY KEY(player_id),
 CONSTRAINT fk_team
 FOREIGN KEY(team_id)
 REFERENCES team(team_id)
 );
  
  insert into player(player_id, first_name, last_name, team_id)
                                           -> Values('1', 'Thorin', 'Oakenshield', '1');
  insert into player(player_id, first_name, last_name, team_id) Values('2', 'Bilbo', 'Baggins', '1') ;
  insert into player(player_id, first_name, last_name, team_id) Values('3', 'Frodo', 'Baggins', '1') ;
  insert into player(player_id, first_name, last_name, team_id) Values('4', 'Saruman', 'The White', '2') ;
  insert into player(player_id, first_name, last_name, team_id) Values('5', 'Angmar', 'Witch-King', '2') ; 
  insert into player(player_id, first_name, last_name, team_id) Values('6', 'Azog', 'The Defiler', '2') ;
  
  select player_id, first_name, last_name, team_id from player;
