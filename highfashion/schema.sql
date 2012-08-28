drop database if exists highfashion;
create database highfashion;
use highfashion;

drop table if exists message;
create table message (
    id int primary key not null auto_increment,
    app_name varchar(50),
    message varchar(250),
    posted timestamp
);
