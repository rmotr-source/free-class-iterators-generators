-- To create this db run in your terminal:
-- $ sqlite3 pokemon.db < schema.sql

drop table if exists pokemon;
create table pokemon (
  id integer primary key autoincrement,
  name text not null,
  type text not null
);
