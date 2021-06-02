create table Account (
id integer primary key unique NOT NULL,
name varchar(64) NOT NULL,
profile_image varchar(255),
age integer,
text varchar (512), 
is_human bool default true);
